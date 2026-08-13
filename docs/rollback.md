# Production Rollback Procedure

## Purpose

Restore the EcommerceLab application to a previously known-good release as quickly as possible.

---

## Roll back by Git tag

List available release tags:

```bash
git fetch --tags
git tag
```

Checkout a previous release:

```bash
git checkout v1.0.0
```

Rebuild and redeploy from that tag.

---

## Roll back Azure Container Apps to a previous image

Set the previous image tag:

```bash
az containerapp update \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --image ecommercelabacr.azurecr.io/ecommercelab:v1.0.0
```

---

## Roll back by revision (Azure Container Apps)

List revisions:

```bash
az containerapp revision list \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --output table
```

Activate a previous revision:

```bash
az containerapp revision activate \
  --name ecommercelab-app \
  --resource-group rg-ecommercelab-dev \
  --revision <REVISION_NAME>
```

---

## Verification checklist

* Home page loads successfully.
* Login works.
* Products page loads.
* Cart workflow works.
* Health endpoint returns HTTP 200.
* No critical errors in logs.

---

## Post-rollback actions

* Notify stakeholders.
* Record rollback time and version.
* Create an incident ticket.
* Perform root-cause analysis.

---

## Current release references

* Current release: `v1.0.1`
* Previous release: `v1.0.0`
