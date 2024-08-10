from file_uploader.file_uploader import FileUploader
from credentials_constant import DirectoryPath, AWSCredentials, GCSCredentials

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
        s3_types=['jpg', 'jpeg', 'png', 'svg', 'webp', 'mp3', 'mp4', 'mpeg4', 'wmv', '3gp', 'webm'],
        gcs_types=['doc', 'docx', 'csv', 'pdf']
    )
