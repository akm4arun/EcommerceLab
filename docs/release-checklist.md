# Production Release Checklist

## Pre-release

* [ ] Feature branch merged into `develop`
* [ ] CI validation workflow passed
* [ ] Unit tests passed
* [ ] Integration tests passed
* [ ] Database migration reviewed
* [ ] Rollback plan confirmed
* [ ] Release notes prepared
* [ ] Docker image built successfully
* [ ] Docker image pushed to Azure Container Registry
* [ ] Security review completed

---

## Release preparation

* [ ] Create release branch or PR from `develop` to `main`
* [ ] Obtain reviewer approval
* [ ] Verify production environment variables
* [ ] Verify production secrets
* [ ] Confirm target Azure resource group
* [ ] Confirm target Azure Container App

---

## Deployment

* [ ] Merge PR into `main`
* [ ] Create Git tag (for example `v1.0.2`)
* [ ] Push Git tag to GitHub
* [ ] Start GitHub Actions deployment
* [ ] Approve production deployment in GitHub Environment
* [ ] Wait for deployment to complete successfully

---

## Post-deployment verification

* [ ] Home page returns HTTP 200
* [ ] Login works
* [ ] Product catalog loads
* [ ] Cart operations work
* [ ] Checkout workflow works
* [ ] Database connectivity verified
* [ ] Application logs checked
* [ ] No critical alerts in Azure Monitor

---

## Rollback readiness

* [ ] Previous Git tag identified
* [ ] Previous container image tag identified
* [ ] Previous Container App revision identified
* [ ] Rollback commands tested in non-production

---

## Release sign-off

| Role            | Name | Status |
| --------------- | ---- | ------ |
| Developer       |      |        |
| Tester          |      |        |
| Reviewer        |      |        |
| Release Manager |      |        |

---

## Current environment

* Environment: `production`
* Azure Resource Group: `rg-ecommercelab-dev`
* Container App: `ecommercelab-app`
* Container Apps Environment: `ecommercelab-env`
* Container Registry: `ecommercelabacr`
* Region: `centralindia`
