data "azurerm_resource_group" "app" {
  name = "rg-ecommercelab-dev"
}

data "azurerm_container_app_environment" "app" {
  name                = "ecommercelab-env"
  resource_group_name = data.azurerm_resource_group.app.name
}

data "azurerm_container_registry" "app" {
  name                = "ecommercelabacr"
  resource_group_name = data.azurerm_resource_group.app.name
}

data "azurerm_postgresql_flexible_server" "app" {
  name                = "ecommercelab-pg"
  resource_group_name = data.azurerm_resource_group.app.name
}