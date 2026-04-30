"""
Data preprocessing helper file for demand forecasting project.
Add reusable cleaning functions here.
"""

import pandas as pd


def clean_demand_data(df):
    """
    Basic cleaning function for product demand dataset.
    """
    df = df.copy()

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Remove invalid dates
    df = df.dropna(subset=["Date"])

    # Clean Order_Demand column
    df["Order_Demand"] = (
        df["Order_Demand"]
        .astype(str)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["Order_Demand"] = pd.to_numeric(df["Order_Demand"], errors="coerce")
    df = df.dropna(subset=["Order_Demand"])

    return df


def create_monthly_series(df, product_code=None, warehouse=None):
    """
    Create monthly demand series.
    """
    data = df.copy()

    if product_code is not None:
        data = data[data["Product_Code"] == product_code]

    if warehouse is not None:
        data = data[data["Warehouse"] == warehouse]

    monthly_series = data.groupby(pd.Grouper(key="Date", freq="ME"))["Order_Demand"].sum()

    return monthly_series
