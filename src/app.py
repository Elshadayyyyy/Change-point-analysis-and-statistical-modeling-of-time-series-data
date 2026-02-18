from flask import Flask, jsonify
from flask_cors import CORS
import logging
from src.data_loader import load_prices, load_events, load_change_points
from src.analysis_service import calculate_summary_statistics

def create_app() -> Flask:
    """Create and configure the Flask app."""
    app = Flask(__name__)
    CORS(app)
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    try:
        prices = load_prices()
        events = load_events()
        change_points = load_change_points()
        logger.info("Data successfully loaded.")
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise
    @app.route("/")
    def home():
        return jsonify({"status": "Brent Oil API is running"}), 200
    @app.route("/prices")
    def get_prices():
        """Return Brent oil prices as JSON."""
        return prices.to_json(orient="records", date_format="iso"), 200
    @app.route("/events")
    def get_events():
        """Return key historical events as JSON."""
        return events.to_json(orient="records", date_format="iso"), 200
    @app.route("/change_points")
    def get_change_points():
        """Return detected change points as ISO dates."""
        return jsonify([d.isoformat() for d in change_points]), 200
    @app.route("/summary")
    def get_summary():
        """Return analytical summary statistics."""
        try:
            summary = calculate_summary_statistics(prices, change_points)
            return jsonify(summary), 200
        except Exception as e:
            logger.error(f"Error generating summary: {e}")
            return jsonify({"error": "Failed to generate summary"}), 500
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
