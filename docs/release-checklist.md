# EcommerceLab Release Checklist

## Purpose

This document provides the release checklist for deploying the EcommerceLab application to Azure Container Apps.

The checklist covers the complete release process from Pull Request validation through production deployment, smoke testing, revision promotion, and rollback.

---

## Release Flow

```text
Developer Change
      |
      v
Create Feature Branch
      |
      v
Pull Request
      |
      v
Validation Pipeline
      |
      v
PR Review and Approval
      |
      v
Merge to main
      |
      v
Build Docker Image
      |
      v
Push Image to ACR
      |
      v
Capture Previous Known-good Revision
      |
      v
Deploy New Container App Revision
      |
      v
Smoke Test
      |
      +----------------------+
      |                      |
    PASS                   FAIL
      |                      |
      v                      v
Promote New             Automatic
Revision                 Rollback
      |                      |
      v                      v
100% Traffic          Previous Revision
                           100%
      |                      |
      +----------+-----------+
                 |
                 v
          Verify Deployment
```

---

## 1. Pre-Release Checks

Before creating a release:

- [ ] Confirm the required code changes are complete.
- [ ] Confirm the application runs correctly in the development environment.
- [ ] Confirm the Dockerfile and application startup configuration are valid.
- [ ] Confirm required database migration changes are included when applicable.
- [ ] Confirm no debugging commands or temporary test changes remain.
- [ ] Confirm secrets and environment-specific configuration are not committed to the repository.
- [ ] Confirm the working tree contains only the intended changes.

Check the Git status:

```bash
git status
```

---

## 2. Create and Push Feature Branch

Create or switch to the appropriate feature branch:

```bash
git checkout -b feature/<feature-name>
```

After making changes:

```bash
git status
```

Review the changes:

```bash
git diff
```

Check for whitespace errors:

```bash
git diff --check
```

Commit the changes:

```bash
git add <files>
git commit -m "<commit-message>"
```

Push the feature branch:

```bash
git push -u origin feature/<feature-name>
```

---

## 3. Pull Request Validation

Create a Pull Request targeting the appropriate branch.

For the main release path:

```text
feature branch
      |
      v
main
```

Confirm the Pull Request includes:

- [ ] Clear description of the change.
- [ ] Relevant testing information.
- [ ] No unrelated changes.
- [ ] Required reviewers assigned.

The validation workflow should complete successfully.

The validation workflow performs application validation and Terraform validation.

### Terraform validation

The Terraform validation job performs:

```bash
terraform fmt -check -recursive
terraform init -input=false
terraform validate
```

The Pull Request should not be merged if required validation checks fail.

---

## 4. Pull Request Approval and Merge

Before merging:

- [ ] Required reviews are complete.
- [ ] All required GitHub Actions checks are passing.
- [ ] No unresolved review comments remain.
- [ ] The Pull Request contains only the intended release changes.

Merge the Pull Request into `main`.

---

## 5. Production Deployment

A push to `main` triggers the Container App deployment workflow.

The deployment workflow performs the following operations:

1. Authenticate to Azure using GitHub OIDC.
2. Verify Azure access.
3. Install application dependencies.
4. Run PostgreSQL migrations.
5. Login to Azure Container Registry.
6. Build the Docker image.
7. Push the Docker image to ACR.
8. Capture the previous known-good Container App revision.
9. Deploy the new Container App revision.
10. Capture the new revision.
11. Run the smoke test.
12. Promote the new revision if the smoke test succeeds.
13. Roll back if the smoke test fails.
14. Display deployment revision evidence.

---

## 6. Verify Previous Known-good Revision

Before the new revision is promoted, the deployment workflow captures the current production revision.

The current revisions can be inspected manually with:

```bash
az containerapp revision list \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --query "[].{name:name,traffic:properties.trafficWeight,state:properties.provisioningState}" \
  -o table
```

The revision receiving 100% traffic is the current production revision.

This revision provides the rollback target if the new deployment fails its smoke test.

---

## 7. New Revision Deployment

The deployment workflow builds the image using the GitHub commit SHA:

```text
ecommercelabacr.azurecr.io/ecommercelab:<GITHUB_SHA>
```

The image is pushed to Azure Container Registry.

The Container App is then updated with the new image:

```bash
az containerapp update \
  --name "$CONTAINER_APP_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --image "$ACR_NAME.azurecr.io/$IMAGE_NAME:${{ github.sha }}"
```

The new revision should be captured by the workflow after deployment.

---

## 8. Smoke Test

The newly deployed revision is tested before receiving production traffic.

The smoke test sends an HTTP request to the new revision's FQDN.

Expected result:

```text
HTTP/1.1 200 OK
```

The smoke test must pass before the new revision is promoted.

### Successful smoke test

```text
New revision
     |
     v
Smoke test
     |
     v
HTTP 200
     |
     v
Promote revision
```

---

## 9. Successful Promotion

When the smoke test succeeds, the deployment workflow promotes the new revision to 100% traffic.

The workflow uses:

```bash
az containerapp ingress traffic set \
  --name "$CONTAINER_APP_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --revision-weight "$NEW_REVISION=100"
```

Verify the traffic distribution:

```bash
az containerapp revision list \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --query "[].{name:name,traffic:properties.trafficWeight,state:properties.provisioningState}" \
  -o table
```

Expected result:

```text
NEW_REVISION    100    Provisioned
```

---

## 10. Automated Rollback

If the smoke test fails:

```text
Smoke test
     |
     v
Failure
     |
     v
Rollback previous revision
     |
     v
Previous revision = 100%
     |
     v
Deployment marked failed
```

The workflow executes:

```bash
az containerapp ingress traffic set \
  --name "$CONTAINER_APP_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --revision-weight "$PREVIOUS_REVISION=100"
```

The new failed revision is not promoted.

The GitHub Actions workflow is marked as failed.

### Important

A failed deployment does not necessarily mean production is unavailable.

The rollback mechanism is designed to restore traffic to the previous known-good revision before the workflow is marked as failed.

---

## 11. Manual Rollback

If an immediate rollback is required outside the deployment workflow, follow the procedure documented in:

```text
docs/rollback.md
```

The basic rollback command is:

```bash
az containerapp ingress traffic set \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --revision-weight "<KNOWN_GOOD_REVISION>=100"
```

After the rollback, verify:

```bash
az containerapp revision list \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --query "[].{name:name,traffic:properties.trafficWeight,state:properties.provisioningState}" \
  -o table
```

Then verify application health:

```bash
curl -i --max-time 30 "https://<REVISION_FQDN>/"
```

Expected:

```text
HTTP/1.1 200 OK
```

---

## 12. Post-Deployment Verification

After a successful deployment:

- [ ] GitHub Actions deployment workflow completed successfully.
- [ ] Docker image was successfully built.
- [ ] Docker image was pushed to ACR.
- [ ] New Container App revision was created.
- [ ] Smoke test passed.
- [ ] New revision received 100% traffic.
- [ ] New revision is in `Provisioned` state.
- [ ] Application endpoint returns a successful HTTP response.
- [ ] Previous revision remains available for rollback if required.

Check revisions:

```bash
az containerapp revision list \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --query "[].{name:name,traffic:properties.trafficWeight,state:properties.provisioningState}" \
  -o table
```

---

## 13. Production Release Completion

The release can be considered complete when:

- [ ] Pull Request was approved and merged.
- [ ] Validation workflow passed.
- [ ] Production deployment workflow passed.
- [ ] New revision was successfully deployed.
- [ ] Smoke test passed.
- [ ] New revision has 100% traffic.
- [ ] Application health was verified.
- [ ] No deployment errors remain.
- [ ] Previous known-good revision remains available for rollback.

---

## 14. Release Failure Criteria

The release should be considered unsuccessful when:

- The build fails.
- The Docker image cannot be pushed to ACR.
- Azure authentication fails.
- The Container App revision cannot be deployed.
- The new revision cannot be identified.
- The smoke test fails.
- Automatic rollback fails.
- The application remains unhealthy after rollback.

If the smoke test fails but automatic rollback succeeds, the release is still considered **failed**, but production traffic should be restored to the previous known-good revision.

---

## 15. Rollback Validation

The automated rollback mechanism has been validated by intentionally causing a smoke-test failure.

The validation confirmed:

1. A new revision was deployed.
2. The smoke test failed.
3. The rollback step was triggered.
4. The previous known-good revision received 100% traffic.
5. The failed revision remained at 0% traffic.
6. The deployment workflow was marked as failed.

The successful deployment path has also been validated:

1. A new revision was deployed.
2. The smoke test returned HTTP 200.
3. The rollback step was skipped.
4. The new revision was promoted to 100% traffic.
5. The deployment workflow completed successfully.

---

## 16. Release Evidence

For each production release, retain the following evidence where appropriate:

- Pull Request reference.
- Git commit SHA.
- GitHub Actions workflow run.
- Docker image tag.
- Previous known-good revision.
- New revision.
- Smoke-test result.
- Final traffic distribution.
- Rollback information if rollback occurred.

This information helps with troubleshooting, incident investigation, and release auditing.

---

## Current Environment

| Item | Value |
|---|---|
| Environment | `production` |
| Azure Resource Group | `rg-ecommercelab-dev` |
| Container App | `ecommercelab-app` |
| Container Apps Environment | `ecommercelab-env` |
| Container Registry | `ecommercelabacr` |
| Region | `centralindia` |

## Release Roles

| Role | Name | Status |
|---|---|---|
| Developer | | |
| Tester | | |
| Reviewer | | |
| Release Manager | | |

## Important Operational Notes

- Do not manually modify production traffic unless required for an operational rollback.
- Always identify the target revision before assigning 100% traffic.
- Do not delete a known-good revision while it may still be required for rollback.
- Do not commit secrets, `.env` files, Terraform state files, or credentials.
- Do not leave debugging commands or intentionally failing smoke-test endpoints in the production workflow.
- If an automated rollback occurs, investigate the failed revision before attempting another deployment.
- Record the reason for a manual production rollback.
- Follow `docs/rollback.md` for the detailed rollback procedure.
