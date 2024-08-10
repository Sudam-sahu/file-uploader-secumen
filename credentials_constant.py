import os
from dotenv import load_dotenv
from pathlib import Path


# Load environment variables
env_path = Path('/path/to/your/.env')
load_dotenv(dotenv_path=env_path)

class DirectoryPath:
    DIRECTORY_PATH = os.getenv('DIRECTORY_PATH')


class AWSCredentials:
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')


class GCSCredentials:
    GCS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')
    GCS_CREDENTIALS_PATH = os.getenv('GCS_CREDENTIALS_PATH')
