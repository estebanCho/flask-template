from flask import Blueprint
from flask_restx import Api

from .test import api as ns_test

api_version = "v1"
blueprint = Blueprint('blueprint_' + api_version, __name__, url_prefix="/" + api_version)

api = Api(blueprint, title=api_version + "API")
api.add_namespace(ns_test)
