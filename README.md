# Formula 1 Hybrid Cloud Data Ingestion & Analytics Pipeline

## Project Overview
This project fulfills the Summer 2026 Data Engineering final project guidelines at SRH University. The goal was to build a dual-pipeline ingestion engine processing F1 data from an Object Store (AWS S3) and a Relational Database (Neon PostgreSQL) to fulfill two distinct business analytics objectives.

### Group Architecture Breakdown:
* **Snowflake Pipeline:** Built a cloud data warehouse using Snowpipe for automated streaming file ingestion from S3, alongside custom Python batch ETL scripts to capture relational tables from Neon. Outputted via a native Streamlit Dashboard application.
* **Databricks Pipeline:** Built a Medallion architecture (Bronze -> Silver -> Gold layers) utilizing Apache Spark and Databricks Auto Loader to automatically ingest stream data, serving out downstream analytics.

---

## Business Objectives Covered
1. **Constructor Performance Analysis:** Evaluating which racing teams score the highest volumes of points over time.
2. **Driver & Pit Stop Impact Analysis:** Uncovering the statistical correlation between average pit stop durations and total career points earned.

---

## Live Dashboard Result
Below is the screenshot of the fully operational Streamlit analytics application:

![Streamlit Dashboard](image_247222.jpg)

---

## Data Source
* Raw dataset source provided courtesy of the **Kaggle Formula 1 Dataset**.
