
# Data-Engineering Zoomcamp 2024 Module 2 Homework

The github repository consists of the files that are submitted as a part of the module 2 homework. 

## Background
In this homework, students were exposed to a mage orchestrator consisting of a data loader, transformer and data exporter block.

## Objective
The objective was to load, transform and export data on green taxi rides within New York City. 

The files for green taxi rides can be downloaded from the following URL: 

https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green/download


## Project Tree

``` tree
.
|-- green_taxi_etl
|    |-- __pycache__
|    |     |-- __init__.cpython-310.pyc
|    |
|    |-- __init__.py
|    |-- metadata.yaml
|
|-- data loaders
|    |-- load_green_taxi_data.py (load green taxi data from API)
|
|-- transformers
|    |-- transform_rows.py (perform transformations)
|
|-- data exporters
|    |-- taxi_to_partitioned_parquet.py (export data to partitioned parquet files)
|    |-- postgres_data_exporter.sql (load data to Postgres SQL database)

```  







