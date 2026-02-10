# Brent oil price change point analysis

## Project overview
This project analyzes historical Brent oil prices (May 1987 – Sep 2022) to detect structural changes in price behavior and associate them with major geopolitical, economic, and policy events. Insights from this analysis support investors, policymakers, and energy companies in understanding risk and planning strategies in volatile energy markets.

## Data
- events.csv — curated dataset of 15 key events (geopolitical, economic, OPEC policy, sanctions)  
- Brent price data should be placed in data/brent_prices.csv 

## Analysis workflow

1. Load and preprocess Brent oil price data  
2. Perform exploratory data analysis (EDA) and visualize trends & volatility  
3. Transform prices into log returns and test stationarity  
4. Prepare data for Bayesian change point modeling (Task 2)  
5. Compare detected change points with curated events  
6. Visualize results and plan for an interactive dashboard (Task 3)

## to clone follow this steps

- clone the repo(git clone https://github.com/Elshadayyyyy/Change-point-analysis-and-statistical-modeling-of-time-series-data.git)
- install requitements pip install -r requirements.txt
- open jupyter notebook(jupyter notebook)
- cd src  
- python app.py  
- cd brent-dashboard  
- npm install  
- npm start  
- Open in your browser: http://localhost:3000  
## Dashboard Features
- Interactive price timeline
- Event based annotations
- Change point indicators
- Clean analytical visuals