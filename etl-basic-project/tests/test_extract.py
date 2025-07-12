# test/test_extract.py

import pandas as pd
from etl.extract import extract_data


def test_extract_valid_csv():
    df = extract_data("data/source_data.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty