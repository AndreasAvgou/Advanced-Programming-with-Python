# 📈 Automated Investment Portfolio Management

This project implements a Python-based system for financial data analysis, portfolio management, and price forecasting. It utilizes **Pandas** for time-series analysis, **OOP** for modeling financial assets, and **Scikit-Learn** for basic machine learning forecasting.

---

## 📌 Project Overview

The goal is to process the `finance_dataset.csv` file to analyze asset performance, detect trends, optimize portfolio allocation based on risk, and predict future prices.

### Key Features:
* **Data Processing:** Load financial data, handle missing values, and detect high volatility periods.
* **Technical Analysis:** Calculate Rolling Moving Averages and detect trend changes (crossovers).
* **OOP Architecture:** `Asset` and `Portfolio` classes to manage investments and calculate risk.
* **Optimization:** Heuristic algorithm (Inverse Volatility) to suggest optimal portfolio weights.
* **Forecasting:** Linear Regression model to predict future asset prices.

---

## 📂 Repository Structure
```
"Assignment_3_Finance/
│
├── finance_dataset.csv         # Input dataset
├── main.py                     # Entry point
├── config.py                   # Settings & paths
├── data_loader.py              # Task 1: Data ingestion & Volatility
├── analytics.py                # Task 2: Rolling Windows & Trends
├── models.py                   # Task 3: OOP Classes (Asset, Portfolio)
├── forecasting.py              # Task 4: ML Forecasting
└── README.md                   # Documentation"
```
---

## ⚙️ Prerequisites

* Python 3.x
* Libraries: `pandas`, `numpy`, `matplotlib`, `scikit-learn`

To install dependencies:
```bash
pip install pandas numpy matplotlib scikit-learn
```

### Expected Output
The script will output:
* **Volatility Analysis:** Alerts for days with returns exceeding the threshold (e.g., >5%).
* **Trend Detection:** Identification of points where price crosses the moving average.
* **Portfolio Optimization:** Calculated risk per asset and suggested allocation percentages (e.g., AAPL: 40%, GOOG: 60%).
* **Forecast:** Predicted prices for the next 5 days for a selected asset.
* **Plots:** Saved in `results/plots/`:
    * `forecast_{ASSET_NAME}.png`: Visualizing actual vs predicted prices.



---

## 📊 Modules Description

### 1. `data_loader.py`
Handles CSV loading, forward-filling missing prices, and calculating daily percentage returns to flag volatility.

### 2. `analytics.py`
Computes Rolling Averages (Smoothing) and generates trading signals based on simple crossover logic.

### 3. `models.py`
* **`Asset`:** Represents a stock, calculating its historical average return and standard deviation (Risk).
* **`Portfolio`:** Aggregates assets and calculates "Inverse Volatility Weights" to minimize risk exposure.

### 4. `forecasting.py`
Uses `LinearRegression` to fit a trend line on the asset's price history and extrapolates it for future days.
