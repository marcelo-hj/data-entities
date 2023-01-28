from pyspark import DataFrame

try:
    from notebooks.base_entities import SnowflakeConnector
    from notebooks.base_entities import GoogleDriveConnector

    from notebooks.base_entities import SparkUtils
except ModuleNotFoundError:
    ...

class CsvToWarehouse:
    def __init__(self, parameters: dict):
        self.source_connector    = parameters['source_connector']
        self.warehouse_connector = parameters['warehouse_connector']

    def extract(self):
        ...

    def transform(self, df: DataFrame):
        ...

    def load(self, df: DataFrame):
        ...

    def run(self) -> None:
        self.load(self.transform(self.extract()))
        ...


params = {
    'warehouse_connector': SnowflakeConnector,
    'source_connector': GoogleDriveConnector
}

load_class = CsvToWarehouse(params)
load_class.run()
