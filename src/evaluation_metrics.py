"""
Evaluation metrics helper file.
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


def calculate_metrics(actual, predicted):
    """
    Calculate MAE, RMSE, and MAPE.
    """
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))

    actual_array = np.array(actual)
    predicted_array = np.array(predicted)

    non_zero = actual_array != 0
    if non_zero.sum() > 0:
        mape = np.mean(np.abs((actual_array[non_zero] - predicted_array[non_zero]) / actual_array[non_zero])) * 100
    else:
        mape = np.nan

    return mae, rmse, mape
