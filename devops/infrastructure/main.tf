provider "azurerm" {
  features {}

}

resource "azurerm_resource_group" "example" {
  name     = "rg-function-app"
  location = "Central US"
  
  # Protect against accidental deletion
  lifecycle {
    prevent_destroy = true
  }
}

resource "azurerm_storage_account" "example" {
  name                     = "funcappstorage1234www" # Change to a globally unique name
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  depends_on = [azurerm_resource_group.example]

  # Ensure atomicity
  lifecycle {
    create_before_destroy = true
  }
}

resource "azurerm_service_plan" "example" {
  name                = "function-app-service-plan"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku_name            = "EP1" # Define the SKU name directly
  os_type             = "Windows" # Specify the OS type

  depends_on = [azurerm_storage_account.example]
}

resource "azurerm_application_insights" "example" {
  name                = "funcapp-insights"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  application_type    = "web"

  depends_on = [azurerm_service_plan.example]
}

resource "azurerm_windows_function_app" "example" {
  name                       = "function-app-exampled2cdd"
  location                   = azurerm_resource_group.example.location
  resource_group_name        = azurerm_resource_group.example.name
  service_plan_id            = azurerm_service_plan.example.id
  storage_account_name       = azurerm_storage_account.example.name
  storage_account_access_key = azurerm_storage_account.example.primary_access_key
  https_only                 = true

  site_config {
    ftps_state = "Disabled" # Example setting; modify as needed
  }

  app_settings = {
    "APPLICATIONINSIGHTS_CONNECTION_STRING" = azurerm_application_insights.example.connection_string
    "FUNCTIONS_WORKER_RUNTIME"              = "dotnet" # Update based on your runtime (e.g., python, node)
  }

  identity {
    type = "SystemAssigned"
  }

  depends_on = [azurerm_application_insights.example]

  # Ensure atomicity
  #lifecycle {
    #prevent_destroy = true
  #}
}
