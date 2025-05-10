from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .config("spark.hadoop.hive.metastore.client.factory.class", "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory") \
    .config("spark.sql.catalogimplementation","hive") \
    .getOrCreate()
conf = spark.sparkContext.getConf()
print("spark.app.name = ", conf.get("spark.hadoop.hive.metastore.client.factory.class"))
print("spark.master = ", conf.get("spark.master"))
print("spark.executor.memory = ", conf.get("spark.executor.memory"))
   # Read data from the database
df = spark.sql("show databases")
df.show()
    
df = spark.sql("select * from productsdb.products limit 10")
df.show() 
print(df.count())