# Container App Rollback Procedure

## Purpose

This document describes the rollback procedure for the EcommerceLab Azure Container App.

The deployment pipeline uses Azure Container Apps revisions to safely deploy new application versions and automatically restore the previous known-good revision when the smoke test fails.

---

## Deployment Strategy

The deployment process follows this sequence:

1. Build the Docker image.
2. Push the image to Azure Container Registry.
3. Capture the current production revision as the previous known-good revision.
4. Deploy a new Container App revision.
5. Capture the new revision name.
6. Run a smoke test against the new revision.
7. If the smoke test passes, promote the new revision to 100% traffic.
8. If the smoke test fails, route 100% traffic back to the previous known-good revision.
9. Mark the GitHub Actions workflow as failed when rollback is triggered.

### Deployment flow

```text
Build
  |
  v
Push image to ACR
  |
  v
Capture previous known-good revision
  |
  v
Deploy new revision
  |
  v
Capture new revision
  |
  v
Smoke test
  |
  +--------------------+
  |                    |
 PASS                 FAIL
  |                    |
  v                    v
Promote new       Rollback to
revision           previous revision
  |                    |
  v                    v
100% traffic       100% traffic
                         |
                         v
                  Mark deployment
                     as failed
```

---

## Manual Rollback Procedure

Use the manual rollback procedure when the currently deployed production revision has an issue and traffic needs to be restored to a known-good revision.

### Prerequisites

Before performing a manual rollback:

- Ensure you are logged in to Azure CLI.
- Confirm the correct subscription is selected.
- Confirm the Container App name and resource group.
- Identify a healthy, previously known-good revision.
- Do not route traffic to a revision that is failed or unhealthy.

### 1. Login to Azure

If required:

```bash
az login
```

Verify the active subscription:

```bash
az account show -o table
```

If multiple subscriptions are available, select the required subscription:

```bash
az account set --subscription "<SUBSCRIPTION_ID>"
```

### 2. List Container App revisions

Run:

```bash
az containerapp revision list \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --query "[].{name:name,traffic:properties.trafficWeight,state:properties.provisioningState}" \
  -o table
```

Example:

```text
Name                          Traffic    State
------------------------------------------------
ecommercelab-app--00000024       0      Provisioned
ecommercelab-app--00000035       0      Provisioned
ecommercelab-app--00000036     100      Provisioned
```

Identify the revision that should receive production traffic.

The selected revision should be:

- A previously known-good revision.
- In `Provisioned` state.
- Known to have passed application health checks.

### 3. Roll back production traffic

Replace `<KNOWN_GOOD_REVISION>` with the revision that should receive production traffic.

```bash
az containerapp ingress traffic set \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --revision-weight "<KNOWN_GOOD_REVISION>=100"
```

Example:

```bash
az containerapp ingress traffic set \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --revision-weight "ecommercelab-app--00000024=100"
```

This routes 100% of production traffic to the selected revision.

The problematic revision remains available but receives 0% traffic.

### 4. Verify traffic distribution

Run:

```bash
az containerapp revision list \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --query "[].{name:name,traffic:properties.trafficWeight,state:properties.provisioningState}" \
  -o table
```

Expected result:

```text
Name                          Traffic    State
------------------------------------------------
KNOWN_GOOD_REVISION            100      Provisioned
CURRENT_BAD_REVISION             0      Provisioned
```

The exact revision names will depend on the current deployment.

### 5. Get the revision FQDN

Run:

```bash
az containerapp revision show \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --revision <KNOWN_GOOD_REVISION> \
  --query properties.fqdn \
  -o tsv
```

Copy the returned FQDN.

### 6. Verify the application

Run:

```bash
curl -i --max-time 30 "https://<REVISION_FQDN>/"
```

A healthy application should return an HTTP success response such as:

```text
HTTP/1.1 200 OK
```

### 7. Confirm the rollback

The rollback is considered successful when:

- The known-good revision has 100% traffic.
- The problematic revision has 0% traffic.
- The known-good revision is `Provisioned`.
- The application endpoint responds successfully.

---

## Automated Rollback

The GitHub Actions deployment workflow performs rollback automatically when the smoke test fails.

### Smoke Test

The smoke-test step uses:

```yaml
id: smoke_test
continue-on-error: true
```

This allows the workflow to continue to the rollback step when the smoke test fails.

The rollback step runs only when:

```yaml
if: steps.smoke_test.outcome == 'failure'
```

### Rollback command used by the pipeline

The workflow executes:

```bash
az containerapp ingress traffic set \
  --name "$CONTAINER_APP_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --revision-weight "$PREVIOUS_REVISION=100"
```

The previous known-good revision therefore receives 100% of production traffic.

### Workflow failure handling

After rollback, the workflow executes the failure step:

```yaml
if: steps.smoke_test.outcome == 'failure'
```

and exits with:

```bash
exit 1
```

This ensures that:

- Production traffic is restored.
- The failed revision is not promoted.
- The GitHub Actions workflow is marked as failed.
- The deployment cannot be mistaken for a successful release.

---

## Successful Deployment

When the smoke test succeeds:

```yaml
if: steps.smoke_test.outcome == 'success'
```

the workflow promotes the new revision:

```bash
az containerapp ingress traffic set \
  --name "$CONTAINER_APP_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --revision-weight "$NEW_REVISION=100"
```

The new revision then receives 100% of production traffic.

The rollback step is skipped because the smoke test succeeded.

---

## Rollback Validation

The automated rollback path has been validated by intentionally causing a smoke-test failure.

During the validation:

1. A new Container App revision was deployed.
2. The smoke test was intentionally made to fail.
3. The GitHub Actions rollback step was triggered.
4. Traffic was restored to the previous known-good revision.
5. The deployment workflow was marked as failed.

This confirms that the automated rollback path works as designed.

A separate manual rollback is not required for validation because the automated rollback path has already been tested.

---

## Current Deployment Verification

The current production revision can be verified with:

```bash
az containerapp revision list \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --query "[].{name:name,traffic:properties.trafficWeight,state:properties.provisioningState}" \
  -o table
```

The production revision should have:

```text
Traffic    State
100        Provisioned
```

Only a healthy, successfully provisioned revision should receive production traffic.

---

## Important Notes

- A rollback changes traffic; it does not delete the failed revision.
- Keep the previous known-good revision available until the deployment has been fully validated.
- Do not delete revisions that may still be required for rollback.
- Verify both traffic distribution and application health after a manual rollback.
- The GitHub Actions workflow is the primary automated deployment and rollback mechanism.
- Manual rollback should be used when immediate traffic restoration is required outside the normal deployment pipeline.
- Always verify the target revision before assigning it 100% production traffic.
- Record the rollback reason and affected revision when performing a production rollback.