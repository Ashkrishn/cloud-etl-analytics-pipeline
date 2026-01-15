# Cloud ETL Analytics Pipeline (AWS S3)

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Python and AWS S3. Raw e-commerce transaction data is ingested locally, cleaned and transformed into an analytics-ready dataset, and uploaded to the cloud for downstream analytics and reporting.

## What This Project Demonstrates

* Industry-style project structure (raw vs processed data)
* Python-based ETL pipeline using Pandas
* Data cleaning and business transformations
* Cloud storage using AWS S3
* Automated data upload using boto3

## Architecture

Local CSV → Python ETL → Processed CSV → AWS S3

## Tech Stack

* Python (Pandas)
* AWS S3
* AWS CLI
* boto3
* Git & GitHub

## Project Structure

```
cloud-etl-analytics-pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── etl/
│   ├── etl_pipeline.py
│   └── upload_to_s3.py
├── notebooks/
└── README.md
```

## ETL Workflow

### Extract

* Reads raw transactional data from a CSV file.

### Transform

* Removes records with missing customer identifiers
* Filters invalid quantities
* Creates business fields such as Revenue and OrderDate

### Load

* Saves the processed dataset locally
* Uploads the processed dataset to AWS S3

## How to Run

### Install dependencies

```bash
pip3 install pandas boto3
```

### Run ETL pipeline

```bash
cd etl
python3 etl_pipeline.py
```

### Upload data to S3

```bash
python3 upload_to_s3.py
```

## Notes

* Raw datasets may be excluded from GitHub due to file size.
* This project is intended for portfolio demonstration.

## Future Enhancements

* Add logging and error handling
* Partition data before cloud upload
* Build BI dashboards using Tableau or Power BI
