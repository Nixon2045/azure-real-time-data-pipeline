# src/processing/databricks/process_iot_data.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, window

spark = SparkSession.builder.getOrCreate()

# Leer datos crudos
df = spark.read.option("multiline", "true").json("abfss://data@STORAGE.dfs.core.windows.net/raw/iot-events/*.json")

# Limpiar
df_clean = df.filter(
    (col("temp").between(0, 50)) &
    (col("humidity").between(20, 90))
)

# Agregar por hora y dispositivo
df_agg = df_clean \
    .withColumn("timestamp", col("timestamp").cast("timestamp")) \
    .groupBy("device_id", window("timestamp", "1 hour")).agg(
        avg("temp").alias("avg_temp"),
        avg("humidity").alias("avg_humidity")
    )

# Guardar en zona curated
df_agg.write.mode("overwrite").parquet("abfss://data@STORAGE.dfs.core.windows.net/curated/daily-summary/")