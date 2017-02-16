import os

os.environ["SPARK_HOME"] = "/usr/local/Cellar/apache-spark/1.6.1/libexec"
from operator import add

from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile("file://///Users/vikas/PycharmProjects/SparkCode/text.txt", 1)
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    sc.stop()