import os
import boto3
from google.cloud import storage
from mimetypes import guess_type

class FileUploader:
    def __init__(self, 
                 s3_bucket_name, 
                 gcs_bucket_name, 
                 aws_access_key=None, 
                 aws_secret_key=None, 
                 gcs_credentials_path=None
    ):
        self.s3_bucket_name = s3_bucket_name
        self.gcs_bucket_name = gcs_bucket_name
        
        # Initialize AWS S3 Client
        try:
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key
            )
        except Exception as e:
            print(f"Failed to initialize S3 client: {e}")
            raise

        # Initialize Google Cloud Storage Client
        try:
            self.gcs_client = storage.Client.from_service_account_json(gcs_credentials_path)
            self.gcs_bucket = self.gcs_client.bucket(self.gcs_bucket_name)
        except Exception as e:
            print(f"Failed to initialize GCS client: {e}")
            raise

    def upload_file_to_s3(self, file_path, s3_key):
        try:
            content_type, _ = guess_type(file_path)
            self.s3_client.upload_file(file_path, self.s3_bucket_name, s3_key)
            print(f"Uploaded {file_path} to S3 bucket {self.s3_bucket_name} as {s3_key}")
        except Exception as e:
            print(f"Failed to upload {file_path} to S3: {e}")

    def upload_file_to_gcs(self, file_path, gcs_key):
        try:
            blob = self.gcs_bucket.blob(gcs_key)
            blob.upload_from_filename(file_path)
            print(f"Uploaded {file_path} to GCS bucket {self.gcs_bucket_name} as {gcs_key}")
        except Exception as e:
            print(f"Failed to upload {file_path} to GCS: {e}")

    def upload_files(self, directory, s3_types, gcs_types):
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = file.split('.')[-1].lower()

                if file_ext in s3_types:
                    self.upload_file_to_s3(file_path, os.path.relpath(file_path, directory))
                elif file_ext in gcs_types:
                    self.upload_file_to_gcs(file_path, os.path.relpath(file_path, directory))
                else:
                    print(f"Skipping file {file_path}, unsupported file type.")
