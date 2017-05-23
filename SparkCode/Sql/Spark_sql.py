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

    # creating a temperory view
    df.createOrReplaceTempView('people')

    # running the query into this view
    spark.sql('select * from people').show()

    # creating a global view which can be alive after the session as well
    df.createGlobalTempView("people_global")

    spark.sql('select * from global_temp.people_global').show()

    # rceating the new session to check if view is avaiable
    spark.newSession().sql('select * from global_temp.people_global').show()