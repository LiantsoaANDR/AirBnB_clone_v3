#!/usr/bin/python3
"""Index"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status', methods=['GET'])
def status():
    """Returns API status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieves the number of each object by type"""
    counts = {}
    for classe in classes:
        counts[classe] = storage.count(classes[classe])
    return jsonify(counts)
