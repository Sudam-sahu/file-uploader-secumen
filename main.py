from file_uploader.file_uploader import FileUploader
from constants.credentials_constant import DirectoryPath, AWSCredentials, GCSCredentials
from constants.constants import RequiredUploadTypesForCloud as Types


if __name__ == "__main__":
    uploader = FileUploader(
        s3_bucket_name=AWSCredentials.S3_BUCKET_NAME,
        gcs_bucket_name=GCSCredentials.GCS_BUCKET_NAME,
        aws_access_key=AWSCredentials.AWS_ACCESS_KEY,
        aws_secret_key=AWSCredentials.AWS_SECRET_KEY,
        gcs_credentials_path=GCSCredentials.GCS_CREDENTIALS_PATH
    )

    uploader.upload_files(
        directory=DirectoryPath.DIRECTORY_PATH,
        s3_types=Types.S3_TYPES,
        gcs_types=Types.GCS_TYPES
    )
