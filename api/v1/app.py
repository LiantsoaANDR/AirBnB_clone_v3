#!/usr/bin/python3
"""app"""

from flask import Flask
from flask_cors import CORS
from os import environ
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views, url_prefix='/api/v1')


@app.errorhandler(404)
def not_found(error):
    """Handle 404 error"""
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown app context"""
    storage.close()


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
