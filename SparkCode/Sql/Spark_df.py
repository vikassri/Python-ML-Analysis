
import sys

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SparkSession
    print("Successfully imported Spark Modules")
    sc = SparkContext(conf=SparkConf(), master='local[1]')
    sc.setLogLevel("ERROR")

except ImportError as e:
    print("Can not import Spark Modules", e)
    sys.exit(1)


if __name__ == '__main__':
    spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()
    df = spark.read.json('file:////Users/vikas/Pycharm/Python/SparkCode/data/resources/people.json')
    df.show()   # printing the dataframe

    df.printSchema()  # printing the schema

    df.select('name').show()  # selecting the name from dataframe and printing it

    df.select(df['name'], df['age'] + 1).show()   # select the name and age with increment by 1

    df.filter(df['age'] < 20).show()   # using filter in the dataframe

    df.groupBy(df['age']).count().show()  # using groupBY in the dataframe
