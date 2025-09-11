# Azure Real-Time Data Pipeline

Proyecto de extremo a extremo que simula una tubería de datos en tiempo real en Azure, desde la ingesta hasta la visualización.

## Arquitectura

![Arquitectura](docs/architecture.png)

- **Ingesta**: Event Hubs recibe eventos de sensores IoT
- **Almacenamiento**: ADLS Gen2 (zona raw → processed)
- **Procesamiento**: Databricks con PySpark
- **Visualización**: Power BI
- **IaC**: Terraform
- **CI/CD**: GitHub Actions

## Tecnologías

- Azure: Event Hubs, ADLS Gen2, Databricks, Functions
- Lenguajes: Python
- Herramientas: Terraform, GitHub Actions

## Como ejecutar

1. Despliega infra: `terraform apply`
2. Ejecuta simulador: `python src/simulator/simulate_iot.py`
3. Monitorea Function App y Databricks

## 📊 Dashboard Power BI

👉 [Ver dashboard](https://app.powerbi.com/reportEmbed?reportId=...)

## 📂 Estructura

(Ver arriba)

## 🛡️ Licencia

MIT