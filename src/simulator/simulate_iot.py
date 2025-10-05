## src/simulator/simulate_iot.py
import json
import random
import time
import os
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData

# ==========================================================
# Configuración de entorno
# ==========================================================
# Si OFFLINE no está definida o es 'true', se usará modo simulado (sin Azure)
OFFLINE = os.getenv("OFFLINE", "true").lower() == "true"

# Cadena de conexión y nombre del Event Hub (solo usadas en modo online)
CONNECTION_STR = os.getenv(
    "EVENT_HUB_CONN_STRING",
    "Endpoint=sb://ehns-iot-pipeline.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=..."
)
EVENTHUB_NAME = os.getenv("EVENT_HUB_NAME", "iot-events")

producer = None
if not OFFLINE:
    try:
        producer = EventHubProducerClient.from_connection_string(
            CONNECTION_STR,
            eventhub_name=EVENTHUB_NAME
        )
        print("[INFO] Ejecutando en modo ONLINE - enviando eventos a Azure Event Hub.")
    except Exception as e:
        print(f"[ERROR] No se pudo inicializar conexión con Event Hub: {e}")
        OFFLINE = True  # fallback a modo offline
else:
    print("[INFO] Ejecutando en modo OFFLINE - los eventos no se enviarán a Azure.")


# ==========================================================
# Generador de eventos simulados
# ==========================================================
def generate_event():
    """Genera un evento IoT simulado."""
    return {
        "device_id": f"sensor-{random.randint(1, 5)}",
        "temp": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(40, 80), 2),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }


# ==========================================================
# Envío o simulación de eventos
# ==========================================================
def send_event(event):
    """Envía un evento al Event Hub o lo simula localmente."""
    if producer:
        try:
            event_data_batch = producer.create_batch()
            event_data_batch.add(EventData(json.dumps(event)))
            producer.send_batch(event_data_batch)
            print(f"[ONLINE] Enviado a Event Hub: {event}")
        except Exception as e:
            print(f"[ERROR] No se pudo enviar el evento: {e}")
    else:
        print(f"[OFFLINE] Evento simulado: {event}")


# ==========================================================
# Loop principal de simulación
# ==========================================================
if __name__ == "__main__":
    try:
        with producer if producer else DummyContextManager():
            while True:
                event = generate_event()
                send_event(event)
                time.sleep(5)
    except KeyboardInterrupt:
        print("Simulación detenida.")


# ==========================================================
# Dummy context manager (solo para modo offline)
# ==========================================================
class DummyContextManager:
    """Permite usar 'with producer' aunque no exista conexión a Azure."""
    def __enter__(self): return self
    def __exit__(self, *args): pass
