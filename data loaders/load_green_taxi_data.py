import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    df = pd.DataFrame()

    for month in [10,11,12]:

        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz'
    
        taxi_dtypes={'VendorID':'Int64',
        'store_and_fwd_flag':str,
        'RatecodeID':'Int64',
        'PULocationID':'float64',
        'DOLocationID':'Int64',
        'passenger_count':'Int64',
        'trip_distance':'float64',
        'fare_amount':'float64',
        'extra':'float64',
        'mta_tax':'float64',
        'tip_amount':'float64',
        'tolls_amount':'float64',
        'improvement_surcharge':'float64',
        'total_amount':'float64',
        'payment_type':'Int64',
        'trip_type':'Int64',
        'congestion_surcharge':'float64'
        }
        
        parse_dates_green_taxi = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

        df = pd.concat([df, pd.read_csv(url, sep=',', dtype=taxi_dtypes, parse_dates=parse_dates_green_taxi)],
        ignore_index=True)
        
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
