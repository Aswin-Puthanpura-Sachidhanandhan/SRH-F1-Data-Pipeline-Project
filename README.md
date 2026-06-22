# Formula 1 Hybrid Cloud Data Ingestion & Analytics Pipeline

## 📌 Project Overview
This project fulfills the Data Engineering final project requirements. The objective was to build a dual-pipeline ingestion engine processing F1 data from an Object Store (AWS S3) and a Relational Database (Neon PostgreSQL) to drive two distinct business analytics dashboards.

## 🏗️ Architecture Breakdown
* **Snowflake/AWS Pipeline:** Built a cloud data warehouse using Snowpipe for automated streaming file ingestion from S3, outputted via a native Streamlit Dashboard application.
* **Databricks Engine:** Engineered a Medallion architecture (Bronze -> Silver -> Gold layers) utilizing Apache Spark and Databricks Auto Loader for advanced data transformations.
* **Neon PostgreSQL Serverless:** Configured a scalable relational database instance to serve the structured historical data for the downstream extraction processes.

---

## 📊 Key Business Outcomes

### 1. Constructor Performance Analysis
**1. Analytics Dashboard (Constructor Performance)** *Brief: Visualizes aggregated F1 constructor data to identify points leaders and race dominance patterns.*
![Constructor Performance](Snowflake_Pipeline/dashboard_obj1.jpg.png)

### 2. Driver & Pit Stop Impact
**2. Analytics Dashboard (Pit Stop Impact)** *Brief: Analyzes the statistical correlation between driver performance and pit stop efficiency metrics.*
![Pit Stop Impact Analysis](Snowflake_Pipeline/dashboard_obj2.jpg.png)

---
*For detailed technical evidence, including automated ingestion proofs, SQL logic, DDL statements, and pipeline extraction scripts, please navigate to the respective `Snowflake_Pipeline` and `Neon_Pipeline` directories.*
