resource "azurerm_storage_account" "storage" {
  name                     = "stiotpipeline${var.suffix}"
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true  # Activa el modo Hierarchical Namespace (ADLS Gen2)
}