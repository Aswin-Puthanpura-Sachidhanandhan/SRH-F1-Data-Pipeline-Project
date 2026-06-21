-- 1. Create a home for your data
CREATE DATABASE IF NOT EXISTS srh_f1_project;
USE DATABASE srh_f1_project;
CREATE SCHEMA IF NOT EXISTS data_pipeline;
USE SCHEMA data_pipeline;

-- 2. Create an empty table to hold F1 driver info
CREATE OR REPLACE TABLE f1_results (
    resultId INT,
    raceId INT,
    driverId INT,
    constructorId INT,
    number STRING,
    grid INT,
    position STRING,
    points FLOAT,
    laps INT,
    time STRING,
    milliseconds STRING,
    fastestLap STRING
);

-- 3. Tell Snowflake how to log into your friend's toy box (S3 Bucket)
CREATE OR REPLACE STAGE f1_s3_stage
  URL = 's3://f1-dataset-mani/'
  CREDENTIALS = (
    AWS_access_key_id = 'YOUR_ACCESS_KEY_HERE'
    AWS_secret_access_key = 'YOUR_SECRET_KEY_HERE'
  )
  FILE_FORMAT = (
    TYPE = 'CSV' 
    SKIP_HEADER = 1 
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  );

-- 4. THE TEST: Ask Snowflake to peer inside the toy box
LIST @f1_s3_stage;

-- 5. Set up the automated pipe (Snowpipe)
CREATE OR REPLACE PIPE f1_results_pipe
  AUTO_INGEST = TRUE
  AS
  COPY INTO f1_results
  FROM @f1_s3_stage/RAW/
  FILES = ('results.csv');


-- 1. Create the two new supporting tables
CREATE OR REPLACE TABLE f1_races (
    raceId INT,
    year INT,
    round INT,
    circuitId INT,
    name STRING,
    date STRING,
    time STRING,
    url STRING,
    fp1_date STRING,
    fp1_time STRING,
    fp2_date STRING,
    fp2_time STRING,
    fp3_date STRING,
    fp3_time STRING,
    quali_date STRING,
    quali_time STRING,
    sprint_date STRING,
    sprint_time STRING
);

CREATE OR REPLACE TABLE f1_drivers (
    driverId INT,
    driverRef STRING,
    number STRING,
    code STRING,
    forename STRING,
    surname STRING,
    dob STRING,
    nationality STRING,
    url STRING
);

-- 2. Create automated Snowpipes for the new files
CREATE OR REPLACE PIPE f1_races_pipe AUTO_INGEST = TRUE AS
  COPY INTO f1_races FROM @f1_s3_stage/RAW/ FILES = ('races.csv');

CREATE OR REPLACE PIPE f1_drivers_pipe AUTO_INGEST = TRUE AS
  COPY INTO f1_drivers FROM @f1_s3_stage/RAW/ FILES = ('drivers.csv');

-- 3. Run the initial data copy command for the new tables
COPY INTO f1_races FROM @f1_s3_stage/RAW/ FILES = ('races.csv');
COPY INTO f1_drivers FROM @f1_s3_stage/RAW/ FILES = ('drivers.csv');  

-- 1. Create the missing tables for Constructors and Pit Stops
CREATE OR REPLACE TABLE f1_constructors (
    constructorId INT,
    constructorRef STRING,
    name STRING,
    nationality STRING,
    url STRING
);

CREATE OR REPLACE TABLE f1_pit_stops (
    raceId INT,
    driverId INT,
    stop INT,
    lap INT,
    time STRING,
    duration STRING,
    milliseconds INT
);

-- 2. Create automated Snowpipes for the new files (FIXED SYNTAX)
CREATE OR REPLACE PIPE f1_constructors_pipe AUTO_INGEST = TRUE AS
  COPY INTO f1_constructors FROM @f1_s3_stage/RAW/ PATTERN = '.*constructors.csv';

CREATE OR REPLACE PIPE f1_pit_stops_pipe AUTO_INGEST = TRUE AS
  COPY INTO f1_pit_stops FROM @f1_s3_stage/RAW/ PATTERN = '.*pit_stops.csv';

-- 3. Run the initial data copy command (FILES is allowed here)
COPY INTO f1_constructors FROM @f1_s3_stage/RAW/ FILES = ('constructors.csv');
COPY INTO f1_pit_stops FROM @f1_s3_stage/RAW/ FILES = ('pit_stops.csv');

-- Set the correct folders
USE DATABASE srh_f1_project;
USE SCHEMA data_pipeline;

-- FORCE all 5 files to load fresh data and ignore any tiny CSV typos
COPY INTO f1_results FROM @f1_s3_stage/RAW/ FILES = ('results.csv') FORCE = TRUE ON_ERROR = 'CONTINUE';
COPY INTO f1_constructors FROM @f1_s3_stage/RAW/ FILES = ('constructors.csv') FORCE = TRUE ON_ERROR = 'CONTINUE';
COPY INTO f1_pit_stops FROM @f1_s3_stage/RAW/ FILES = ('pit_stops.csv') FORCE = TRUE ON_ERROR = 'CONTINUE';
COPY INTO f1_races FROM @f1_s3_stage/RAW/ FILES = ('races.csv') FORCE = TRUE ON_ERROR = 'CONTINUE';
COPY INTO f1_drivers FROM @f1_s3_stage/RAW/ FILES = ('drivers.csv') FORCE = TRUE ON_ERROR = 'CONTINUE';