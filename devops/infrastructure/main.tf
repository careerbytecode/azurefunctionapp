provider "azurerm" {
  features {}

  subscription_id = var.subscription_id
  tenant_id       = var.tenant_id
  client_id       = var.client_id
  client_secret   = var.client_secret
}

resource "azurerm_resource_group" "example" {
  name     = "rg-function-app"
  location = "Central US"

  lifecycle {
    prevent_destroy = true
  }
}

resource "azurerm_storage_account" "example" {
  name                     = "funcappstorage1234www"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_service_plan" "example" {
  name                = "function-app-service-plan"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku_name            = "EP1"
  os_type             = "Windows"
}

resource "azurerm_application_insights" "example" {
  name                = "funcapp-insights"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  application_type    = "web"
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
    ftps_state = "Disabled"
  }

  app_settings = {
    "APPLICATIONINSIGHTS_CONNECTION_STRING" = azurerm_application_insights.example.connection_string
    "FUNCTIONS_WORKER_RUNTIME"              = "dotnet"
  }

  identity {
    type = "SystemAssigned"
  }
}
