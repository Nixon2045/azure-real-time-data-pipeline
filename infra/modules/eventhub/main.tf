resource "azurerm_eventhub_namespace" "eh" {
  name                = "ehns-iot-pipeline"
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = "Standard"
  capacity            = 1
}

resource "azurerm_eventhub" "hub" {
  name                = "iot-events"
  namespace_id        = azurerm_eventhub_namespace.eh.id  
  partition_count     = 2
  message_retention   = 1
}
