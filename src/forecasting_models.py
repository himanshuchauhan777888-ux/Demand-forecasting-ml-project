"""
Forecasting model helper file.
Keep functions simple and aligned with the notebook workflow.
"""

import pandas as pd


def seasonal_naive_forecast(train_series, forecast_periods=6, season_length=12):
    """
    Seasonal naive forecast using previous season values.
    """
    last_season = train_series.iloc[-season_length:]
    forecast_values = []

    for i in range(forecast_periods):
        forecast_values.append(last_season.iloc[i % season_length])

    return forecast_values


def moving_average_forecast(train_series, forecast_periods=6, window=12):
    """
    Moving average forecast using last window average.
    """
    avg_value = train_series.iloc[-window:].mean()
    return [avg_value] * forecast_periods
