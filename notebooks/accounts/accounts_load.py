from notebooks.connectors.aws_s3_connector import AwsBucketConnector
from notebooks.base_entities.csv_to_warehouse import CsvToWarehouse
from notebooks.connectors.snowflake_connector import SnowflakeConnector

source_connector = AwsBucketConnector(
    container='data-lake-cold',
    folder='accounts',
    file_extension='csv'
)
warehouse_connector = ...

params = {
    'entity': 'accounts',
    'warehouse_connector': warehouse_connector,
    'source_connector': source_connector
}

load_class = CsvToWarehouse(params)
load_class.run()
