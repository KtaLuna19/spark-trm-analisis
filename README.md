Se busca identificar estadísticas clave como:
- Promedio del valor del dólar
- Valor mínimo y máximo
- Distribución de los datos

## Fuente de datos

El conjunto de datos utilizado corresponde a registros históricos de la TRM en Colombia, almacenados en formato CSV.

## Tecnologías utilizadas

- Apache Spark
- Python (PySpark)
- Hadoop HDFS
- Linux (Ubuntu)

##  Ejecución del proyecto

### 1. Iniciar Hadoop
start-dfs.sh


### 2. Ejecutar el script en Spark
spark-submit tareapy

##  Resultados obtenidos

- Total de registros: 8230
- Promedio TRM: ~2355 COP
- Valor mínimo: 620.62 COP
- Valor máximo: 5061.21 COP

##  Autor: Catalina Usuga Arenas

Proyecto académico - Análisis de Big Data con Apache Spark
