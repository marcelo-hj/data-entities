class AwsBucketConnector:
    def __init__(self, container: str, folder: str, file_extension: str):
        self.container = container
        self.folder = folder
        self.file_extension = file_extension

    def source_path(self) -> str:
        file_path = f'https://{self.container}.s3.sa-east-1.amazonaws.com/' \
                    f'{self.folder}/*.{self.file_extension}'
        return file_path
