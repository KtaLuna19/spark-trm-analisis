from pyspark.sql import SparkSession

# Crear sesión de Spark
spark = SparkSession.builder.appName("Analisis TRM Colombia").getOrCreate()

# Cargar datos desde HDFS
df = spark.read.csv("hdfs://localhost:9000/Tarea3/rows.csv", header=True, inferSchema=True)

print("=== ESTRUCTURA DEL DATASET ===")
df.printSchema()

print("=== PRIMEROS DATOS ===")
df.show(20, False)

print("=== TOTAL DE REGISTROS ===")
total = df.count()
print("Total de registros:", total)

print("=== ESTADISTICAS GENERALES ===")
df.describe().show()

print("=== VALOR MAXIMO DEL DOLAR ===")
df.orderBy(df.VALOR.desc()).show(5)

print("=== VALOR MINIMO DEL DOLAR ===")
df.orderBy(df.VALOR.asc()).show(5)

# Detener Spark
spark.stop()
