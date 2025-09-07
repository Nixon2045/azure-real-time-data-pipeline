output "storage_account_name" {
  value = module.datalake.storage_account_name
}

output "eventhub_connection_string" {
  value = module.eventhub.eventhub_connection_string  
}

output "databricks_workspace_url" {
  value = module.databricks.databricks_workspace_url
}