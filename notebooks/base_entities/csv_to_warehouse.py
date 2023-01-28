from pyspark.sql import DataFrame

try:
    from notebooks.connectors.snowflake_connector import SnowflakeConnector
    from notebooks.connectors.aws_s3_connector import AwsBucketConnector
    from notebooks.utils.notebook_utils import SparkUtils

except ModuleNotFoundError:
    ...


class CsvToWarehouse:
    def __init__(self, parameters: dict):
        self.entity = parameters['entity']
        self.source_connector = parameters['source_connector']
        self.warehouse_connector = parameters['warehouse_connector']

        self.spark_session = SparkUtils(
            session_name=f'{self.entity}-csv-to-warehouse',
            configs=[]
        ).get_session()

    def extract(self) -> DataFrame:
        file_path = self.source_connector.source_path()

        df = (self.spark_session.
              read.
              format('csv').
              load(file_path))

        return df

    def transform(self, df: DataFrame) -> DataFrame:
        df.display()

        return df

    def load(self, df: DataFrame) -> None:
        ...

    def run(self) -> None:
        self.load(self.transform(self.extract()))


params = {
    'warehouse_connector': SnowflakeConnector,
    'source_connector': AwsBucketConnector
}

load_class = CsvToWarehouse(params)
load_class.run()
