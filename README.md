# Sacumen File-Uploader Project

The Sacumen project is a Python application for uploading files to AWS S3 and Google Cloud Storage (GCS) based on their file types. It utilizes the AWS SDK for Python (`boto3`) and the Google Cloud Storage client library. Environment variables are managed via a `.env` file for secure credential handling.

## Prerequisites

- **Python 3.9**: Ensure Python 3.9 is installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/release/python-390/).
- **pip**: The package installer for Python (usually comes with Python).

## Project Structure

The project directory structure is as follows:

```
sacumen-project/
│
├── file_uploader/
│ ├── __init__.py
│ └── file_uploader.py
│
├── constants/
│ ├── __init__.py
│ ├── credentials_constant.py
│ └── constants.py
│
├── main.py
├── .env
├── requirements.txt
```

- **`file_uploader/`**: Contains the `file_uploader.py` module responsible for uploading files to AWS S3 and GCS.
- **`constants/`**: Contains configuration files including `credentials_constant.py` for environment variable management and `constants.py` for additional constants.
- **`main.py`**: The main script that initiates the file upload process.
- **`.env`**: File for storing environment variables.
- **`requirements.txt`**: Lists the Python dependencies required for the project.


## Installation and Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/sacumen-project.git
cd sacumen-project

python3.9 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Set Up the .env File

```bash
# AWS S3 Credentials
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_S3_BUCKET_NAME=your-s3-bucket

# Google Cloud Storage Credentials
GCS_BUCKET_NAME=your-gcs-bucket
GCS_CREDENTIALS_PATH=/path/to/your/gcs/credentials.json

# Directory Path
DIRECTORY_PATH=/path/to/your/directory
```

### 3. Run the Project

```bash
python main.py
```

### 4. Deactivate the Virtual Environment

Once you're done, you can deactivate the virtual environment:

```bash
deactivate
```
