output "eventhub_connection_string" {
  value = azurerm_eventhub_namespace.eh.default_primary_connection_string
  sensitive = true
}