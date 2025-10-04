# src/ingestion/__init__.py
import logging
import json
import datetime
from azure.storage.filedatalake import DataLakeServiceClient

def main(event) -> None:
    message = event.get_body().decode('utf-8')
    logging.info(f"Evento recibido: {message}")

    try: 
        data = json.loads(message)
        save_to_adls(data)
    except Exception as e:
        logging.error(f"Error procesando evento: {e}")

def save_to_adls(data):
    account_name = "stiotpipelineXXXXXX"  # desde Terraform
    file_system_name = "data"
    directory_name = "raw/iot-events"
    file_name = f"{directory_name}/event-{datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S-%f')}.json"

    service_client = DataLakeServiceClient(
        account_url=f"https://{account_name}.dfs.core.windows.net",
        credential="YOUR_ACCESS_KEY"  # Mejor: Managed Identity o SAS
    )

    file_system_client = service_client.get_file_system_client(file_system_name)
    file_client = file_system_client.get_file_client(file_name)
    file_client.create_file()
    file_client.append_data(json.dumps(data), offset=0)
    file_client.flush_data(len(json.dumps(data)))