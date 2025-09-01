output "storage_account_name" {
  value = azurerm_storage_account.storage.name
}

output "eventhub_connection_string" {
  value = azurerm_eventhub_namespace.eh.default_primary_connection_string
  sensitive = true
}

output "databricks_workspace_url" {
  value = azurerm_databricks_workspace.dbr.workspace_url
}