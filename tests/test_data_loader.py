import pytest
import pandas as pd
from src.data_loader import load_prices, load_events, load_change_points

def test_load_prices():
    df = load_prices()
    assert isinstance(df, pd.DataFrame), "Prices should be a DataFrame"
    assert "Date" in df.columns, "Prices DataFrame must have 'Date' column"
    assert not df.empty, "Prices DataFrame should not be empty"
    assert df["Date"].is_monotonic_increasing, "Dates should be sorted ascending"
def test_load_events():
    df = load_events()
    assert isinstance(df, pd.DataFrame), "Events should be a DataFrame"
    assert "Date" in df.columns, "Events DataFrame must have 'Date' column"
    assert not df.empty, "Events DataFrame should not be empty"
def test_load_change_points():
    cps = load_change_points()
    assert isinstance(cps, list), "Change points should be a list"
    import pandas as pd
    assert pd.api.types.is_datetime64_any_dtype(pd.Series(cps)), "All change points should be Timestamps"
    assert len(cps) > 0, "There should be at least one change point"
