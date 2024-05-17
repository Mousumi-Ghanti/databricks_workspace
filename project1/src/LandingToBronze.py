# Databricks notebook source
# MAGIC %sql
# MAGIC DESCRIBE EXTERNAL LOCATION `landing-zone`

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

landing_data = spark.read.json("s3://databricks-development-ext-ws-bkt-767397898349/landing/")
display(landing_data)
landing_data.printSchema()

# COMMAND ----------

schema_converted_data = landing_data.withColumn("time_stamp", to_timestamp("timestamp_str")).drop("timestamp_str").withColumn("secret_val", col("secret").cast("string")).drop("secret")
display(schema_converted_data)
schema_converted_data.printSchema()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE `databricks_main_ws`.`bronze`.`NIFI_EVENT`
# MAGIC (
# MAGIC   `id` STRING, `time_stamp` TIMESTAMP, `secret_val` STRING, `active` BOOLEAN
# MAGIC );

# COMMAND ----------

schema_converted_data.write.mode("overwrite").saveAsTable('`databricks_main_ws`.`bronze`.`NIFI_EVENT`')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from `databricks_main_ws`.`bronze`.`NIFI_EVENT` limit 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) as RecCount from `databricks_main_ws`.`bronze`.`NIFI_EVENT`;

# COMMAND ----------


