from flask import Flask, jsonify
from flask_cors import CORS
from src.data_loader import load_prices, load_events, load_change_points

def create_app() -> Flask:
    """Create and configure the Flask app."""
    app = Flask(__name__)
    CORS(app)
    prices = load_prices()
    events = load_events()
    change_points = load_change_points()
    @app.route("/")
    def home():
        return jsonify({"status": "Brent Oil API is running"})
    @app.route("/prices")
    def get_prices():
        """Return Brent oil prices as JSON."""
        return prices.to_json(orient="records", date_format="iso")
    @app.route("/events")
    def get_events():
        """Return key historical events as JSON."""
        return events.to_json(orient="records", date_format="iso")
    @app.route("/change_points")
    def get_change_points():
        """Return detected change points as ISO dates."""
        return jsonify([d.isoformat() for d in change_points])
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
