#!/usr/bin/python3
""" Views module
"""
from api.v1.views.index import status  # Updated
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


app_views.add_url_rule(
    "/status", methods=["GET"], view_func=status)  # << added
