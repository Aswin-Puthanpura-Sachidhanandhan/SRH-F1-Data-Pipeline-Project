import os
import pandas as pd
from sqlalchemy import create_engine
import boto3
from io import StringIO

# Securely fetch credentials from GitHub Secrets
neon_url = os.environ['NEON_URL']
AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
S3_BUCKET_NAME = 'f1-dataset-mani'

engine = create_engine(neon_url)
s3_resource = boto3.resource(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

tables_to_sync = ['drivers', 'results', 'pit_stops', 'constructors']

for table in tables_to_sync:
    try:
        print(f"Extracting '{table}'...")
        df = pd.read_sql(f"SELECT * FROM {table};", engine)
        
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        
        file_name = f"neon_{table}.csv"
        s3_resource.Object(S3_BUCKET_NAME, file_name).put(Body=csv_buffer.getvalue())
        print(f"✅ Pushed '{file_name}' to S3.")
    except Exception as e:
        print(f"⚠️ Skipped '{table}'.")