if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

import os
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd


#define the OS environment id
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/home/src/terraform-demo-435315-133b467bd115.json'

#define bucket name
bucket_name='mage-zoomcamp-vksatiyam'

#define the table name
table_name='nyc_green_taxi_data'

#define project ID
project_id='terraform-demo-435315'

root_path=f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here

    #convert datetime column to date 
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    #convert our pandas df to parquet table
    table = pa.Table.from_pandas(data)

    #define the gcs filesystem
    gcs = pa.fs.GcsFileSystem()

    #write the table to gcs filesystem
    # Write the table to GCS filesystem
    pq.write_to_dataset(
        table=table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )



