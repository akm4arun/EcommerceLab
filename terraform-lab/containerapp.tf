resource "azurerm_container_app" "app" {
  name                         = "ecommercelab-app"
  resource_group_name          = data.azurerm_resource_group.app.name
  container_app_environment_id = data.azurerm_container_app_environment.app.id
  revision_mode                = "Multiple"

  max_inactive_revisions = 100
  workload_profile_name  = "Consumption"

  lifecycle {
    ignore_changes = [
      secret,
      template[0].container[0].command
    ]
  }

  ingress {
    external_enabled           = true
    target_port                = 8000
    allow_insecure_connections = false

    traffic_weight {
      percentage      = 100
      revision_suffix = "0000024"
      latest_revision = false
    }
  }

  registry {
    server               = data.azurerm_container_registry.app.login_server
    username             = data.azurerm_container_registry.app.admin_username
    password_secret_name = "ecommercelabacrazurecrio-ecommercelabacr"
  }

  template {
    container {
      name   = "ecommercelab-app"
      image  = "ecommercelabacr.azurecr.io/ecommercelab:b729d652d1db86f9c6b409b3f1625801c35574e1"
      cpu    = 0.5
      memory = "1Gi"

      env {
        name        = "DATABASE_URL"
        secret_name = "pgurl"
      }
    }
  }
}