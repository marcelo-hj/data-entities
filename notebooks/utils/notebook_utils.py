from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

from typing import List


class SparkUtils:
    def __init__(self, session_name: str, configs: List[tuple] = None):
        self.session_name = session_name
        self.configs = configs

    def get_session(self) -> SparkSession:
        spark_configs = SparkConf().setAll(self.configs)

        spark = (SparkSession.
                 builder.
                 master('local[-1]').
                 appName(self.session_name).
                 config(spark_configs).
                 getOrCreate())

        return spark
