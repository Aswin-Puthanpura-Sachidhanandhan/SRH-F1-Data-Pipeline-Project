# Neon PostgreSQL Relational Database Setup

This section documents the creation and validation of the serverless PostgreSQL environment used as the relational source for the hybrid architecture.

### 1. Data Extraction Logic (Colab)
*Brief: Illustrates the Python-based extraction process used to pull raw data securely from the Neon environment.*
![Colab Script](colab_script.jpg.png)

### 2. Database Schema Creation (DDL)
*Brief: Execution of the DDL statements in the Neon SQL Editor to construct the core relational tables (`drivers` and `races`).*
![Table Creation Logic](neon_table_creation.png.png)

### 3. Relational Data Verification
*Brief: Validating the relational database environment by displaying the structured driver schema and verifying the successful load of 861 rows.*
![Driver Data View](neon_data_populated.png.png)  
![Row Count Validation](neon_row_count.png.png)
