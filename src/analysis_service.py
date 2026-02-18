from typing import Dict
import pandas as pd
import numpy as np

def calculate_summary_statistics(
    prices_df: pd.DataFrame,
    change_points: list
) -> Dict:
    """
    Calculate summary statistics for Brent oil prices.

    Args:
        prices_df (pd.DataFrame): DataFrame containing price data.
        change_points (list): List of detected change point dates.

    Returns:
        Dict: Summary statistics dictionary.
    """
    total_records = len(prices_df)
    date_range = {
        "start": str(prices_df["Date"].min()),
        "end": str(prices_df["Date"].max())
    }
    max_price = float(prices_df["Price"].max())
    min_price = float(prices_df["Price"].min())
    prices_df["log_return"] = np.log(prices_df["Price"]).diff()
    annual_volatility = float(prices_df["log_return"].std() * np.sqrt(252))
    return {
        "total_price_records": total_records,
        "date_range": date_range,
        "number_of_change_points": len(change_points),
        "max_price": max_price,
        "min_price": min_price,
        "average_annual_volatility": round(annual_volatility, 4)
    }
