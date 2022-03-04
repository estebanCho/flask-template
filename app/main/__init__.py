from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging
from app.main.config.app_config import config_by_name


db = SQLAlchemy()


def register_extensions(flask_app: Flask):
    from app.main.common.extensions import cors

    cors.init_app(flask_app)


def register_routers(flask_app: Flask):
    from .controller import blueprint
    flask_app.register_blueprint(blueprint)


def register_hooks(flask_app: Flask):
    from app.main.common.exception_handler import broad_exception_handler
    from app.main.common.request_context import after_request, before_request

    flask_app.before_request(before_request)
    flask_app.after_request(after_request)
    flask_app.register_error_handler(Exception, broad_exception_handler)


def create_app(config_name) -> Flask:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03dZ %(message)s',
                        datefmt="%Y-%m-%dT%H:%M:%S", )

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)

    register_extensions(app)
    register_routers(app)
    register_hooks(app)

    return app
