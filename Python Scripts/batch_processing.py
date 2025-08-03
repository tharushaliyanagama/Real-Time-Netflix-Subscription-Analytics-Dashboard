from pyspark.sql import SparkSession
import pyarrow.parquet as pq

spark = SparkSession.builder.appName("NetflixBatch").getOrCreate()
df = spark.read.option("header", "true").option("inferSchema", "true").csv("D:\\Netflix Project\\Python Scripts\\Netflix subscription fee Dec-2021.csv")
df = df.select('Country_code', 'Country', 'Cost Per Month - Basic ($)', 'Cost Per Month - Standard ($)', 'Cost Per Month - Premium ($)')
df.write.parquet('D:\\Netflix Project\\Python Scripts\\data_lake\\subscriptions_batch.parquet', mode='overwrite')
spark.stop()
