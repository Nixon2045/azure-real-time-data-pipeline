# src/simulator/simulate_iot.py
import json
import random
import time
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData

# configuracion del Event Hub
CONNECTION_STR = "Endpoint=sb://ehns-iot-pipeline.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=..."  # Reemplaza
EVENTHUB_NAME = "iot-events"

producer = EventHubProducerClient.from_connection_string(CONNECTION_STR, eventhub_name=EVENTHUB_NAME) # Crear el cliente del productor de eventos para Event Hub

def generate_event():
    return {
        "device_id": f"sensor-{random.randint(1, 5)}",
        "temp": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

try:
    with producer:
        while True:
            event_data_batch = producer.create_batch() # Crear un lote de eventos
            event = generate_event()
            event_data_batch.add(EventData(json.dumps(event))) # Convertir a JSON
            producer.send_batch(event_data_batch)
            print(f"Enviado: {event}")
            time.sleep(5)  # evento generado cada 5 segundos
except KeyboardInterrupt:
    print("Simulación detenida.")