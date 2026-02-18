import pandas as pd
import pickle
from pathlib import Path
from typing import List, Tuple

BASE_DIR = Path(__file__).resolve().parent.parent / "Data"
def load_prices() -> pd.DataFrame:
    """Load and preprocess Brent oil prices."""
    prices_path = BASE_DIR / "BrentOilPrices.csv"
    df = pd.read_csv(prices_path)
    df.rename(columns=lambda x: x.strip().capitalize(), inplace=True)
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
    df = df.sort_values("Date")
    return df
def load_events() -> pd.DataFrame:
    """Load and preprocess key historical events."""
    events_path = BASE_DIR / "events.csv"
    events = pd.read_csv(events_path)
    events.rename(columns=lambda x: x.strip().capitalize(), inplace=True)
    events["Date"] = pd.to_datetime(events["Date"])
    return events
def load_change_points() -> List[pd.Timestamp]:
    """Load change points from pickle and convert to Timestamps."""
    cp_path = BASE_DIR / "change_points.pkl"
    with open(cp_path, "rb") as f:
        change_points = pickle.load(f)
    change_points = [pd.to_datetime(d) for d in change_points]
    return change_points
def load_all_data() -> Tuple[pd.DataFrame, pd.DataFrame, List[pd.Timestamp]]:
    """Load prices, events, and change points together."""
    return load_prices(), load_events(), load_change_points()
