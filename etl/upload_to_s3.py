import boto3
import os

# Create S3 client
s3 = boto3.client("s3")

# Update this if your bucket name is slightly different
BUCKET_NAME = "cloud-etl-analytics-ashwin"

# Local file path
FILE_PATH = "../data/processed/online_retail_processed.csv"

# S3 destination path
S3_KEY = "processed/online_retail_processed.csv"

# Upload file
s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)

print("Processed data uploaded to S3 successfully")
