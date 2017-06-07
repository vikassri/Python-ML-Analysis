from __future__ import print_function

from operator import add
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession

print("Successfully imported Spark Modules")
sc = SparkContext(conf=SparkConf(), master='local[1]')

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    lines = spark.read.text('file:////Users/vikas/Pycharm/Python/SparkCode/data/resources/people.txt').rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))
    spark.stop()