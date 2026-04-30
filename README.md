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
├── linkedin_resume/
│   ├── linkedin_post.md
│   └── resume_bullets.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Key Results
Add your final results here after running the notebook.

Example:

| Model | MAE | RMSE | MAPE |
|---|---:|---:|---:|
| Seasonal Naive | Add value | Add value | Add value |
| Moving Average | Add value | Add value | Add value |
| SES | Add value | Add value | Add value |
| Regression + Seasonality | Add value | Add value | Add value |
| Hybrid Model | Add value | Add value | Add value |

## Final Forecast Output
The final model generates a 6-month future demand forecast.  
Forecast results should be saved in:

```text
outputs/results/future_forecast.csv
```

## Business Impact
This forecasting workflow can help businesses:

- Improve inventory planning
- Reduce overstock and stockout risks
- Support production scheduling
- Make data-driven demand planning decisions

## Author
Himanshu
