# Brent Oil Price Change Point Analysis

## Project Overview

This project analyzes historical Brent oil prices (May 1987 – Sep 2022) to **detect structural change points** in price behavior and associate them with major geopolitical, economic, and policy events. Insights from this analysis help **investors, energy analysts, and policymakers** understand market volatility, anticipate risks, and make data-driven decisions.

The backend API has been **refactored for reliability**, with **unit tests**, **automated CI/CD**, and modular design to ensure **reproducibility** and maintainability.

---

## Business Value

- Identify significant market shifts caused by geopolitical events or economic shocks  
- Quantify volatility and detect trends for investment planning  
- Provide a reproducible, automated system that can be extended with additional datasets or forecasting models  
- Present results through an **interactive dashboard** for non-technical stakeholders

---

## Data

- `events.csv` — curated dataset of 15 key historical events  
- `BrentOilPrices.csv` — historical Brent crude price data  
- All datasets are versioned and included in the repository under `/Data`

---

## Analysis Workflow

1. Load and preprocess Brent oil price data  
2. Perform exploratory data analysis (EDA) and visualize trends & volatility  
3. Transform prices into log returns and test for stationarity  
4. Detect change points using Bayesian change point modeling  
5. Compare detected change points with curated events  
6. Serve data via a **REST API (Flask)** for prices, events, and change points  
7. Plan and integrate an **interactive React dashboard** for visualization  

---

## API Endpoints

| Endpoint         | Description                                |
| ---------------- | ------------------------------------------ |
| `/`              | Health check (returns API status)          |
| `/prices`        | Returns all Brent price records            |
| `/events`        | Returns all curated events                 |
| `/change_points` | Returns detected change points (ISO dates) |

> The API is **unit-tested** with `pytest` and integrated with **GitHub Actions CI/CD** for automatic validation.

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/Elshadayyyyy/Change-point-analysis-and-statistical-modeling-of-time-series-data.git
cd Change-point-analysis-and-statistical-modeling-of-time-series-data

# Setup Python environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run Flask API
cd src
python app.py

# Run the React dashboard
cd ../brent-dashboard
npm install
npm start
# Open in browser: http://localhost:3000

# Run tests
pytest -v


## Project Structure
```
week11/
├─ src/
│   ├─ app.py             
│   └─ data_loader.py    
├─ Data/
│   ├─ BrentOilPrices.csv
│   ├─ change_points.pkl
│   └─ events.csv
├─ tests/
│   ├─ test_app_routes.py
│   └─ test_data_loader.py
├─ brent-dashboard/     
├─ requirements.txt
└─ .github/workflows/    
```

## Key Results

* Reliable API: Serves Brent prices, events, and change points
* Automated testing: 8 tests passing, reproducible results with pytest
* CI/CD Integration: Every push validated via GitHub Actions
* Interactive Dashboard: Allows filtering by time range, highlighting change points, and viewing detailed metrics
* Business-ready: Clear presentation for finance analysts and policymakers

## Future Improvements
* Enhance React dashboard with additional visualizations and summaries
* Integrate other economic indicators (e.g., WTI crude, exchange rates)
* Implement forecasting models for risk and investment analysis
* Add model explainability visualizations (e.g., SHAP) for predictive features

