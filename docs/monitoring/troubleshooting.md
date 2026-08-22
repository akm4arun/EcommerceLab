# EcommerceLab Monitoring & Troubleshooting Runbook

## Purpose

This runbook provides the standard troubleshooting procedure for
EcommerceLab Azure Container Apps when Azure Monitor detects application
errors, performance issues, or container restarts.

The monitoring architecture consists of:

- Azure Container Apps
- Log Analytics
- Azure Monitor alerts
- Azure Monitor metrics
- Action Group email notifications

---

# 1. Application HTTP 5xx Errors

## Alert

Alert:

`alert-ecommercelab-application-errors`

The alert monitors `ContainerAppHTTPLogs` and fires when the application
returns one or more HTTP 5xx responses within the five-minute evaluation
window.

## KQL

```kusto
ContainerAppHTTPLogs
| where ContainerAppName == 'ecommercelab-app'
| where TimeGenerated > ago(1h)
| where toint(StatusCode) >= 500
| summarize
    ErrorCount = count(),
    FirstError = min(TimeGenerated),
    LastError = max(TimeGenerated)
    by RevisionName, Path, StatusCode
| order by LastError desc
```

# 2. HTTP 5xx Trend

Use this query to determine whether HTTP 5xx errors are isolated or
occurring repeatedly over time.

## KQL

```kusto
ContainerAppHTTPLogs
| where ContainerAppName == 'ecommercelab-app'
| where TimeGenerated > ago(1h)
| where toint(StatusCode) >= 500
| summarize
    ErrorCount = count()
    by bin(TimeGenerated, 5m), RevisionName, StatusCode
| order by TimeGenerated asc
```

## Interpretation

- A single isolated 500 may indicate an individual application failure.
- Repeated 5xx responses indicate an ongoing application problem.
- A sudden increase after a deployment should be correlated with the active
  revision.

# 3. Identify the Affected Revision

First identify the revisions deployed to the Container App.

## Azure CLI

```bash
az containerapp revision list \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --query "[].{revision:name,created:properties.createdTime,active:properties.active,traffic:properties.trafficWeight,provisioningState:properties.provisioningState}" \
  -o table
```

## What to check

Check the following:

1. Current active revision.
2. Revision receiving traffic.
3. Revision creation time.
4. Provisioning state.
5. Whether the error started after a new revision was deployed.

## Example

```text
Revision                    Traffic    ProvisioningState
ecommercelab-app--0000040   100        Provisioned
```

If the errors started shortly after a new revision received traffic,
investigate that revision first.

# 4. Revision-Specific HTTP Error Investigation

Once the alert identifies a revision, filter the HTTP logs for that
specific revision.

## KQL

```kusto
ContainerAppHTTPLogs
| where ContainerAppName == 'ecommercelab-app'
| where RevisionName == 'ecommercelab-app--0000040'
| where TimeGenerated > ago(1h)
| where toint(StatusCode) >= 500
| project
    TimeGenerated,
    RevisionName,
    Method,
    Path,
    StatusCode,
    RequestDuration,
    ResponseCodeDetails
| order by TimeGenerated desc
```

## Replace

Replace:

```text
ecommercelab-app--0000040
```

with the revision identified by the alert.

## What this identifies

- Failed endpoint.
- HTTP method.
- HTTP status code.
- Request duration.
- Response details.
- Affected revision.

# 5. Application Log Investigation

Use Container App console logs to investigate application-level errors.

## KQL

```kusto
ContainerAppConsoleLogs_CL
| where ContainerAppName_s == 'ecommercelab-app'
| where TimeGenerated > ago(1h)
| where Log_s contains 'ERROR'
    or Log_s contains 'Error'
    or Log_s contains 'Exception'
    or Log_s contains 'Traceback'
| project
    TimeGenerated,
    RevisionName_s,
    ContainerName_s,
    Stream_s,
    Log_s
| order by TimeGenerated desc
| take 50
```

## What to look for

Look for:

- Python exceptions.
- Stack traces.
- Database connection failures.
- Configuration errors.
- Dependency failures.
- Application startup failures.
- Authentication or authorization errors.

The application logs should be investigated together with the HTTP
error logs.

# 6. CPU Investigation

Container Apps exposes CPU utilization through the `CpuPercentage`
metric.

## Azure CLI

```bash
MSYS_NO_PATHCONV=1 az monitor metrics list \
  --resource "/subscriptions/79e2c10d-eb12-40dd-8f8f-65fa6b9ed2d8/resourceGroups/rg-ecommercelab-dev/providers/Microsoft.App/containerApps/ecommercelab-app" \
  --metric CpuPercentage \
  --start-time 2026-08-22T09:19:00Z \
  --end-time 2026-08-22T09:29:00Z \
  --interval PT1M \
  --aggregation Average \
  -o table
```

For a real incident, replace the start and end times with the time window
surrounding the alert.

## What to check

Compare CPU utilization with the time of the HTTP error.

High CPU during the error window may indicate:

- CPU saturation.
- Expensive application processing.
- Increased request load.
- Application performance degradation.

CPU correlation alone does not prove that CPU was the root cause.

# 7. Memory Investigation

Container Apps exposes memory utilization through the
`MemoryPercentage` metric.

## Azure CLI

```bash
MSYS_NO_PATHCONV=1 az monitor metrics list \
  --resource "/subscriptions/79e2c10d-eb12-40dd-8f8f-65fa6b9ed2d8/resourceGroups/rg-ecommercelab-dev/providers/Microsoft.App/containerApps/ecommercelab-app" \
  --metric MemoryPercentage \
  --start-time 2026-08-22T09:19:00Z \
  --end-time 2026-08-22T09:29:00Z \
  --interval PT1M \
  --aggregation Average \
  -o table
```

For a real incident, replace the start and end times with the time window
surrounding the alert.

## What to check

Check whether memory utilization increased around the time of the
application errors.

High memory utilization may indicate:

- Memory pressure.
- Memory leak.
- Large application workload.
- Excessive request processing.

Memory correlation alone does not prove that memory was the root cause.

# 8. Replica Restart Investigation

Container Apps exposes replica restart information through the
`RestartCount` metric.

## Azure CLI

```bash
MSYS_NO_PATHCONV=1 az monitor metrics list \
  --resource "/subscriptions/79e2c10d-eb12-40dd-8f8f-65fa6b9ed2d8/resourceGroups/rg-ecommercelab-dev/providers/Microsoft.App/containerApps/ecommercelab-app" \
  --metric RestartCount \
  --start-time 2026-08-22T09:19:00Z \
  --end-time 2026-08-22T09:29:00Z \
  --interval PT1M \
  --aggregation Maximum \
  -o table
```

## What to check

Determine whether a replica restart occurred during the same time window
as the application error.

A restart may indicate:

- Application crash.
- Container failure.
- Resource-related failure.
- Container lifecycle event.

If `RestartCount` remains zero during the error window, do not attribute
the HTTP error to a container restart.

# 9. Request-Level Investigation

Use `ContainerAppHTTPLogs` to inspect recent requests and identify
potentially problematic endpoints.

## KQL

```kusto
ContainerAppHTTPLogs
| where ContainerAppName == 'ecommercelab-app'
| where TimeGenerated > ago(1h)
| project
    TimeGenerated,
    RevisionName,
    Method,
    Path,
    StatusCode,
    RequestDuration,
    ResponseCodeDetails,
    ReplicaName
| order by TimeGenerated desc
| take 50
```

## What this identifies

- Request timestamp.
- Revision.
- HTTP method.
- Endpoint.
- HTTP status code.
- Request duration.
- Response details.
- Replica information.

# 10. Validate Application Health

Use the application's `/health` endpoint to verify that the application
is currently responding.

First obtain the application FQDN if required.

## Azure CLI

```bash
az containerapp show \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --query properties.configuration.ingress.fqdn \
  -o tsv
```

Then run:

```bash
curl -i --max-time 30 \
  "https://<APPLICATION_FQDN>/health"
```

## Expected response

```text
HTTP/1.1 200 OK
```

Expected application response:

```json
{
  "status": "ok"
}
```

A successful health check confirms that the application is responding to
the health endpoint at the time of the test.

It does not prove that all application functionality is healthy.

# 11. Error to CPU/Memory/Restart Correlation

When the application error alert fires, investigate the same time window
across the available signals.

```text
HTTP 5xx Error
      |
      v
Identify Revision
      |
      v
Identify Endpoint
      |
      +----------------------+
      |                      |
      v                      v
   CPU Usage            Memory Usage
      |                      |
      +----------+-----------+
                 |
                 v
          Replica Restart?
                 |
                 v
          Application Logs
                 |
                 v
             /health
                 |
                 v
        Determine likely cause
```

## Correlation table

| Signal | Observation | Investigation direction |
|---|---|---|
| HTTP 5xx | Error detected | Identify endpoint and revision |
| CPU | High during error | Investigate CPU saturation or expensive processing |
| Memory | High during error | Investigate memory pressure or application memory usage |
| RestartCount | Increased | Investigate crash or container instability |
| Application logs | Exception/Traceback | Investigate application code or dependency |
| New revision | Error started after deployment | Investigate recent deployment changes |
| `/health` | 200 OK | Application is responding to health checks |

Correlation should be treated as investigation evidence, not automatic
proof of root cause.

# 12. Example Troubleshooting Scenarios

## Scenario A - Application Issue After Deployment

```text
HTTP 500       YES
CPU            LOW
Memory         LOW
RestartCount   0
New Revision   YES
```

### Investigation direction

- Compare the error start time with the deployment time.
- Identify the failing endpoint.
- Review application console logs.
- Review changes introduced by the new revision.
- Check database and external dependency connectivity.

### Likely direction

Application-level issue introduced by the deployment.

The application logs and code changes must be reviewed before declaring
the root cause.

## Scenario B - High CPU

```text
HTTP 500       YES
CPU            HIGH
Memory         NORMAL
RestartCount   0
```

### Investigation direction

- Check request volume.
- Identify slow or expensive endpoints.
- Review request duration.
- Review application processing.
- Determine whether CPU saturation coincides with the errors.

## Scenario C - Memory Pressure and Restart

```text
HTTP 500       YES
CPU            NORMAL
Memory         HIGH
RestartCount   INCREASED
```

### Investigation direction

- Check application memory consumption.
- Review application logs before and after the restart.
- Investigate possible memory leaks.
- Check whether the restart occurred before or after the HTTP errors.

## Scenario D - Application Logic or Dependency Failure

```text
HTTP 500       YES
CPU            NORMAL
Memory         NORMAL
RestartCount   0
New Revision   NO
```

### Investigation direction

- Identify the failing endpoint.
- Review application console logs.
- Check database connectivity.
- Check external dependencies.
- Check application configuration.
- Investigate application-level exceptions.

# 13. Troubleshooting Decision Flow

```text
Azure Monitor Alert
        |
        v
HTTP 5xx detected?
        |
        v
Identify Revision + Endpoint
        |
        +-----------------------------+
        |                             |
        v                             v
New deployment?                 Existing revision?
        |                             |
        v                             v
Compare deployment             Investigate application
time with error time            and dependencies
        |
        v
Check Application Logs
        |
        v
Check CPU
        |
        v
Check Memory
        |
        v
Check RestartCount
        |
        v
Run /health
        |
        v
Determine likely cause
        |
        v
Mitigate / Rollback / Fix
```