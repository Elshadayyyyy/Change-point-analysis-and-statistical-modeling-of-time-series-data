# Brent oil price change point analysis
## Project overview

This project analyzes historical Brent oil prices (May 1987 – Sep 2022) to detect structural changes in price behavior and associate them with major geopolitical, economic, and policy events. Insights from this analysis support investors, policymakers, and energy companies in understanding risk and planning strategies in volatile energy markets.
The backend API has been refactored for reliability, with unit tests and automated CI/CD to ensure reproducibility and maintainability.
---

## Data
* events.csv — curated dataset of 15 key events
* BrentOilPrices.csv — historical price data 
---

## Analysis Workflow
1. Load and preprocess Brent oil price data
2. Perform exploratory data analysis (EDA) and visualize trends & volatility
3. Transform prices into log returns and test stationarity
4. Detect change points using Bayesian change point modeling
5. Compare detected change points with curated events
6. Serve data via a REST API (Flask) with endpoints for prices, events, and change points
7. Plan for an interactive dashboard (React)
---

## API Endpoints
| Endpoint         | Description                                |
| ---------------- | ------------------------------------------ |
| `/`              | Health check (returns API status)          |
| `/prices`        | Returns all Brent price records            |
| `/events`        | Returns all curated events                 |
| `/change_points` | Returns detected change points (ISO dates) |
The API is fully tested with pytest and integrated with GitHub Actions CI/CD for automatic verification of functionality.
---

## Quick Start
```bash
# Clone the repository
git clone https://github.com/Elshadayyyyy/Change-point-analysis-and-statistical-modeling-of-time-series-data.git
cd Change-point-analysis-and-statistical-modeling-of-time-series-data
# Create virtual environment and install dependencies
python -m venv venv
venv\Scripts\activate      
pip install -r requirements.txt
# run flask backend
cd src
python app.py
# for the dashboard
cd brent-dashboard
npm install
npm start
# Open in browser: http://localhost:3000
```

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
* API provides reliable access to price data, events, and change points
* All backend logic is unit-tested with pytest (7 tests passing)
* CI/CD integration ensures reproducibility and automatic validation on every push

## Future Improvements
* Add a fully interactive React dashboard with visualizations and change point analysis
* Include additional economic indicators to enhance modeling and correlation analysis
* Incorporate forecasting models for risk and investment planning

