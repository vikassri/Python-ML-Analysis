from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import *


class spark_basics:
    Spark = None

    def __init__(self):
        self.Spark = SparkSession.builder.appName('Spark_Basics').master('local[1]').getOrCreate()

    def get_session(self):
        return self.Spark


if __name__ == '__main__':
    spark = spark_basics().get_session()
    l = [('Alice', 1)]
    d = [{'name': 'Alice', 'Age': 5}]

    """ Create a dataframe from list """
    print(spark.createDataFrame(l).collect())                   # create a Dataframe from RDD
    print(spark.createDataFrame(l,['name', 'age']).collect())   # provide column name to Dataframe

    """ create rdd from the same lists """
    rdd_l = spark.sparkContext.parallelize(l)
    print(spark.createDataFrame(rdd_l, ['name', 'age']).collect())   # create a Dataframe from RDD

    """ Working with row and types """
    Person = Row('name', 'age')
    person = rdd_l.map(lambda x: Person(*x))
    print(spark.createDataFrame(person).collect())

    schema = StructType([StructField('Naam', StringType(), True), StructField('Umar',IntegerType(), True)])
    print(spark.createDataFrame(person,schema).collect())