# Formula 1 Hybrid Cloud Data Ingestion & Analytics Pipeline

## 📌 Project Overview
This project fulfills the Data Engineering final project requirements. The objective was to build a dual-pipeline ingestion engine processing F1 data from an Object Store (AWS S3) and a Relational Database (Neon PostgreSQL) to drive two distinct business analytics dashboards.

## 🏗️ Architecture Breakdown
* **Snowflake/AWS Pipeline:** Built a cloud data warehouse using Snowpipe for automated streaming file ingestion from S3, outputted via a native Streamlit Dashboard application.
* **Databricks Engine:** Engineered a Medallion architecture (Bronze -> Silver -> Gold layers) utilizing Apache Spark and Databricks.
* **Neon PostgreSQL Serverless:** Configured a scalable relational database instance to serve the structured historical data for the downstream extraction processes.

---
## ⚙️ Technologies Used

- Databricks
- Apache Spark
- Delta Lake
- AWS S3
- Neon PostgreSQL
- Python
- SQL


## 📊 Key Business Outcomes
## Snowflake

### 1. Constructor Performance Analysis
**1. Analytics Dashboard (Constructor Performance)** *Brief: Visualizes aggregated F1 constructor data to identify points leaders and race dominance patterns.*
![Constructor Performance](Snowflake_Pipeline/dashboard_obj1.jpg.png)

### 2. Driver & Pit Stop Impact
**2. Analytics Dashboard (Pit Stop Impact)** *Brief: Analyzes the statistical correlation between driver performance and pit stop efficiency metrics.*
![Pit Stop Impact Analysis](Snowflake_Pipeline/dashboard_obj2.jpg.png)

---
##Databricks
## 🔄 Databricks Pipeline Flow

```text
                    ┌─────────────────┐
                    │   AWS S3 CSVs   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Databricks Auto │
                    │     Loader      │
                    └────────┬────────┘
                             │

                    ┌─────────────────┐
                    │ Neon PostgreSQL │
                    │ (Drivers/Races) │
                    └────────┬────────┘
                             │
                             ▼

══════════════════════════════════════════
              BRONZE LAYER
══════════════════════════════════════════

        Raw ingestion from S3 and Neon
        Stored as Delta Tables

                             │
                             ▼

══════════════════════════════════════════
              SILVER LAYER
══════════════════════════════════════════

      Data Cleaning & Transformation

      • Remove duplicates
      • Handle null values
      • Standardize formats
      • Join datasets
      • Validate records

                             │
                             ▼

══════════════════════════════════════════
               GOLD LAYER
══════════════════════════════════════════

      Business Ready Aggregations

      • Driver Rankings
      • Constructor Rankings
      • Total Points
      • Total Wins
      • Avg Pit Stop Duration
      • Avg Finish Position

                             │
                             ▼

══════════════════════════════════════════
             DASHBOARDS
══════════════════════════════════════════

      Dashboard 1
      Top Constructors Performance

      • Constructor Ranking
      • Total Points
      • Total Wins
      • Points Distribution

                             │

      Dashboard 2
      Driver Performance &
      Pit Stop Impact Analysis

      • Driver Rankings
      • Driver Points
      • Pit Stop Analysis
      • Finish Position Analysis

                             │
                             ▼

══════════════════════════════════════════
          DATBRICKS JOBS
══════════════════════════════════════════

      Scheduled Pipeline Execution

      • Refresh Bronze Tables
      • Refresh Silver Tables
      • Refresh Gold Tables
      • Update Dashboards
```


*For detailed technical evidence, including automated ingestion proofs, SQL logic, DDL statements, and pipeline extraction scripts, please navigate to the respective `Snowflake_Pipeline` and `Neon_Pipeline` directories.*
