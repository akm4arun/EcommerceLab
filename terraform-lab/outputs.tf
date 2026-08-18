output "terraform_resource_group_id" {
  description = "ID of the Terraform-managed resource group"
  value       = azurerm_resource_group.lab.id
}

output "terraform_storage_account_id" {
  description = "ID of the Terraform-managed storage account"
  value       = azurerm_storage_account.lab.id
}

output "terraform_storage_account_name" {
  description = "Name of the Terraform-managed storage account"
  value       = azurerm_storage_account.lab.name
}

output "application_container_app_id" {
  description = "ID of the existing EcommerceLab Container App"
  value       = azurerm_container_app.app.id
}

output "application_container_app_name" {
  description = "Name of the existing EcommerceLab Container App"
  value       = azurerm_container_app.app.name
}

output "application_container_app_fqdn" {
  description = "FQDN of the EcommerceLab Container App"
  value       = azurerm_container_app.app.ingress[0].fqdn
}

output "application_container_registry_login_server" {
  description = "ACR login server used by the application"
  value       = data.azurerm_container_registry.app.login_server
}

output "application_postgresql_fqdn" {
  description = "PostgreSQL Flexible Server FQDN"
  value       = data.azurerm_postgresql_flexible_server.app.fqdn
}