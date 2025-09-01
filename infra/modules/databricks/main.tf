resource "azurerm_databricks_workspace" "dbr" {
  name                = "dbr-iot-pipeline"
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = "standard"
  managed_resource_group_name = "rg-dbr-managed-${var.suffix}"
}
