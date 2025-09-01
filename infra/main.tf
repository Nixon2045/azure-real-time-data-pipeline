provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-iot-pipeline"
  location = var.location
}

resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
  numeric = true
}

module "datalake" {
  source              = "./modules/datalake"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  suffix              = random_string.suffix.result
}

module "eventhub" {
  source              = "./modules/eventhub"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
}

module "databricks" {
  source              = "./modules/databricks"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  suffix              = random_string.suffix.result
}