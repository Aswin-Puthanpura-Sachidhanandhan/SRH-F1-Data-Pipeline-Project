# Formula 1 Hybrid Cloud Data Ingestion & Analytics Pipeline

## Project Overview
This project fulfills the Summer 2026 Data Engineering final project requirements at SRH University. The goal was to build a dual-pipeline ingestion engine processing F1 data from an Object Store (AWS S3) and a Relational Database (Neon PostgreSQL) to fulfill two distinct business analytics objectives.

## Evidence & Documentation

**1. Analytics Dashboard (Constructor Performance)**  
*Brief: This dashboard visualizes aggregated F1 constructor data to identify points leaders and race dominance patterns.*  
![Constructor Performance](dashboard_obj1.jpg.png)

**2. Analytics Dashboard (Pit Stop Impact)**  
*Brief: This view analyzes the correlation between driver performance and pit stop efficiency metrics.*  
![Pit Stop Impact Analysis](dashboard_obj2.jpg.png)

**3. Pipeline SQL Logic**  
*Brief: Demonstrates the CREATE TABLE and data ingestion logic executed in Snowflake to maintain the F1 dataset.*  
![SQL Pipeline Logic](pipeline_sql.jpg.png)

**4. Data Extraction Logic (Colab)**  
*Brief: Illustrates the Python-based extraction process used to pull raw relational data securely from the Neon PostgreSQL database.*  
![Colab Script](colab_script.jpg.png)

## Architecture Breakdown
* **Snowflake Pipeline:** Built a cloud data warehouse using Snowpipe for automated streaming file ingestion from S3, alongside custom Python batch ETL scripts to capture relational tables from Neon, outputted via a native Streamlit Dashboard application.
* **Databricks Pipeline:** Built a Medallion architecture (Bronze -> Silver -> Gold layers) utilizing Apache Spark and Databricks Auto Loader to automatically ingest stream data, serving out downstream analytics.

---
*Raw dataset source: Kaggle Formula 1 Dataset.*
