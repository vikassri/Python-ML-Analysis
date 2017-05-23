
import sys

try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    from pyspark.sql import SparkSession
    from pyspark.sql import Row

    print("Successfully imported Spark Modules")
    sc = SparkContext(conf=SparkConf(), master='local[1]')
    sc.setLogLevel("ERROR")

except ImportError as e:
    print("Can not import Spark Modules", e)
    sys.exit(1)


if __name__ == '__main__':
    spark = SparkSession.builder.appName('RDD demo').getOrCreate()
    lines = sc.textFile("file:////Users/vikas/Pycharm/Python/SparkCode/data/resources/people.txt")
    parts = lines.map(lambda l: l.split(','))
    people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

    # create the dataframe from RDD
    peoples_schema = spark.createDataFrame(people)

    # create the schema using dataframe
    ppl = peoples_schema.createOrReplaceTempView('people')

    # SQL can be run over DataFrames that have been registered as a table.
    teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

    # The results of SQL queries are Dataframe objects.
    # rdd returns the content as an :class:`pyspark.RDD` of :class:`Row`.
    teenames =  teenagers.rdd.map(lambda p: "Name: " + p.name).collect()

    # printing the name
    for name in teenames:
        print(name)
