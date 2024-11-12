if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


import re

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    #remove rows where passenger count is 0 and trip distance is 0
    data = data.loc[(data.trip_distance!=0) & (data.passenger_count!=0)]

    #Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    #iterate through columns in data df
    renamed_cols={'VendorID':'vendor_id',
    'RatecodeID':'ratecode_id',
    'PULocationID':'pu_location_id',
    'DOLocationID':'do_location_id'
    }

    #rename columns to convert from camel case to lower snake case
    data.rename(columns=renamed_cols, inplace=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'vendor_id' in list(output), 'vendor_id is not one of the existing values in the column'
    assert output[output['passenger_count']==0].shape[0]==0, 'There are passenger count < 0'
    assert output[output['trip_distance']==0].shape[0]==0, 'There are trip distance < 0'
