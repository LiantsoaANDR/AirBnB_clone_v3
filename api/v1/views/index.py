#!/usr/bin/python3
"""Index"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Returns API status"""
    return jsonify({"status": "OK"})


@app_views.route('/status', methods=['GET'])
def get_stats():
    """Retrieves the number of each object by type"""

    counts = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(counts)
