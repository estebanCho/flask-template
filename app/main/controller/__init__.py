from flask import Blueprint

from .v1 import blueprint as blueprint_v1
# from .v2 import blueprint as blueprint_v2

blueprint = Blueprint('api', __name__)
blueprint.register_blueprint(blueprint_v1)
# blueprint.register_blueprint(blueprint_v2)
