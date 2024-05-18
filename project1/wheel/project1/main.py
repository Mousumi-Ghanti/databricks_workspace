from pyspark.sql import SparkSession, DataFrame

def get_cartoon_data(spark: SparkSession) -> DataFrame:
  return spark.read.csv("/FileStore/tables/data/Cartoon_datasets.csv")

def put_cartoon_data(df: DataFrame):
  return df.write.saveAsTable("`databricks_main_ws`.`bronze`.`cartoon_data`")

def get_spark() -> SparkSession:
  try:
    from databricks.connect import DatabricksSession
    return DatabricksSession.builder.getOrCreate()
  except ImportError:
    return SparkSession.builder.getOrCreate()

def main():
  get_cartoon_data(get_spark())

if __name__ == '__main__':
  main()