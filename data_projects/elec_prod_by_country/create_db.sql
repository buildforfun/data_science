CREATE DATABASE IF NOT EXISTS WorldBankData;
USE WorldBankData;

CREATE TABLE IF NOT EXISTS ElecProdBySource (
    Country VARCHAR(255),
    Coal DOUBLE,
    Natural_gas FLOAT,
    Oil FLOAT,
    Hydropower FLOAT,
    Renewable_sources FLOAT,
    Nuclear FLOAT,
    Access_to_electricity FLOAT
);

LOAD DATA INFILE '/data/processed/3.7_Electricity_production_sources_and_access_processed.csv'
INTO TABLE ElecProdBySource
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Country, @Coal, @Natural_gas, @Oil, @Hydropower, @Renewable_sources, @Nuclear, @Access_to_electricity)
SET 
  Coal = NULLIF(@Coal, ''),
  Natural_gas = NULLIF(@Natural_gas, ''),
  Oil = NULLIF(@Oil, ''),
  Hydropower = NULLIF(@Hydropower, ''),
  Renewable_sources = NULLIF(@Renewable_sources, ''),
  Nuclear = NULLIF(@Nuclear, ''),
  Access_to_electricity = NULLIF(@Access_to_electricity, '');