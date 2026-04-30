# Demand Forecasting using Machine Learning

## Project Overview
This project focuses on forecasting product demand using historical order data.  
The goal is to analyze demand patterns, compare forecasting models, and predict future demand for better inventory and business planning.

## Business Problem
Businesses need accurate demand forecasts to manage inventory, reduce stockouts, avoid overstocking, and improve production planning.  
This project applies time series forecasting techniques to estimate future demand for selected product and warehouse combinations.

## Dataset
The project uses historical product demand data with fields such as:

- Date
- Product_Code
- Warehouse
- Product_Category
- Order_Demand

## Project Workflow

### 1. Data Cleaning
- Converted the Date column into datetime format
- Removed missing or invalid dates
- Cleaned Order_Demand values
- Aggregated demand at monthly level

### 2. Exploratory Data Analysis
- Checked demand trend over time
- Compared product/category demand
- Identified seasonal patterns
- Selected suitable product and warehouse combinations for forecasting

### 3. Model Building
The following forecasting models were used:

- Seasonal Naive Model
- Trailing Moving Average
- Simple Exponential Smoothing
- Regression with Trend and Seasonality
- Hybrid Regression + SES Residual Model

### 4. Model Evaluation
Models were compared using:

- MAE: Mean Absolute Error
- RMSE: Root Mean Squared Error
- MAPE: Mean Absolute Percentage Error, where applicable

### 5. Future Forecasting
The best-performing model was used to forecast upcoming 6 months of demand.

## Tools and Technologies
- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Statsmodels

## Repository Structure

```text
demand-forecasting-ml-project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   ├── 02_model_building_and_comparison.ipynb
│   └── 03_future_forecasting.ipynb
│
├── outputs/
│   ├── plots/
│   └── results/
│
├── src/
│   ├── data_preprocessing.py
│   ├── evaluation_metrics.py
│   └── forecasting_models.py
│
├── docs/
│   └── project_summary.md
│
├── requirements.txt
├── .gitignore
└── README.md
```
## Key Results

| Model | MAE | RMSE | MAPE |
|---|---:|---:|---:|
| Seasonal Naive | 36,536.99 | 43,666.95 | 10.50% |
| Trailing Moving Average | 30,951.83 | 44,604.31 | 8.47% |
| Regression + C(Month) | 17,752.58 | 21,034.51 | 5.35% |
| Regression + trend² + C(Month) | 18,035.20 | 21,152.01 | 5.42% |
| Regression + SES Residuals | 17,622.69 | 21,169.82 | 5.33% |

## Final Model Selection

The **Regression + SES Residuals** model was selected as the final forecasting model because it achieved the lowest MAE and lowest MAPE among all tested models.

This means the model produced the smallest average forecasting error and gave the most accurate percentage-based demand forecast.

## Final Forecast Output

The selected model was used to forecast demand for the upcoming 6 months.  
The forecast output can support inventory planning, production planning, and demand-based business decisions.

## Business Impact
This forecasting workflow can help businesses:

- Improve inventory planning
- Reduce overstock and stockout risks
- Support production scheduling
- Make data-driven demand planning decisions

## Author
Himanshu
