# test/test_transform.py

from etl.extract import extract_data
from etl.transform import transform_data


def test_transform_correct_columns():
    df = extract_data("data/source_data.csv")
    df_transformed = transform_data(df)
    assert df_transformed is not None
    assert "heightinches" in df_transformed.columns
    assert "weightpounds" in df_transformed.columns