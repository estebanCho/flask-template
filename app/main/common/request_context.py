from flask import Response, request
import logging
import json


def after_request(response: Response) -> Response:
    try:
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "deny"
    finally:
        return response


def before_request():
    pass
    # logging.getLogger().info(request)
    # logging.getLogger().info("{0}".format(request.headers.get("X-Request-Id")))
