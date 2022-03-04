from flask import request
import logging
import json
from app.main.common.scheme import LogDict


def log(log_data: dict):
    try:
        data = alterLog(log_data)
        logging.getLogger().info(
            "{} - {} - {} - {} - {} - {}".format(data.get("event"), data.get("request"),
                                                 data.get("response"),
                                                 data.get("internal_result"),
                                                 data.get("internal_error"),
                                                 data.get("internal_function")))
    except Exception as e:
        import traceback

        error_data = {
            "event": "logging_error",
            "internal_error": {"error": "{0}".format(e), "trace": traceback.format_exc()}
        }
        logging.getLogger().error("{} - {} - {} - {} - {} - {}".format(error_data.get("event"), {}, {}, {},
                                                                       json.dumps(error_data.get("internal_error")),
                                                                       {}))


def alterLog(log_data: dict) -> LogDict:
    """
    log_data
        event, response, access_token, db, api_response, api_request, error
    """
    result = {
        "event": log_data.get("event"),
        "request": json.dumps({
            "id": request.headers.get("X-Request-Id"),
            "method": request.method,
            "path": request.path,
            "authorization": log_data.get("access_token") if "access_token" in log_data else {},
            "body": request.json if request.json else {},
            "query_string": request.query_string.decode()
        }),
        "response": json.dumps(log_data.get("response")) if "response" in log_data else {},
        "internal_result": json.dumps({
            "db": log_data.get("db") if "db" in log_data else {},
            "api_response": log_data.get("api_response") if "api_response" in log_data else {},
            "api_request": log_data.get("api_request") if "api_request" in log_data else {}
        }),
        "internal_error": json.dumps(log_data.get("error")) if "error" in log_data else {},
        "internal_function": {}
    }

    return result
