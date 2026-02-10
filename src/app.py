from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
from pathlib import Path
app = Flask(__name__)
CORS(app)
BASE_DIR = Path(__file__).resolve().parent
prices_path = BASE_DIR / "../Data/BrentOilPrices.csv"
df = pd.read_csv(prices_path)
df.rename(columns=lambda x: x.strip().capitalize(), inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
events_path = BASE_DIR / "../Data/events.csv"
events = pd.read_csv(events_path)
events.rename(columns=lambda x: x.strip().capitalize(), inplace=True)
events["Date"] = pd.to_datetime(events["Date"])
cp_path = BASE_DIR / "../Data/change_points.pkl"
with open(cp_path, "rb") as f:
    change_points = pickle.load(f)
change_points = [pd.to_datetime(d) for d in change_points]
@app.route("/prices")
def get_prices():
    return df.to_json(orient="records", date_format="iso")
@app.route("/events")
def get_events():
    return events.to_json(orient="records", date_format="iso")
@app.route("/change_points")
def get_change_points():
    return jsonify([d.isoformat() for d in change_points])
@app.route("/")
def home():
    return jsonify({"status": "Brent Oil API is running"})
if __name__ == "__main__":
    app.run(debug=True)
