from http import HTTPStatus

from flask import current_app, jsonify, request
from pydantic import ValidationError
from werkzeug.exceptions import HTTPException
from app.main.common.log import log


# error 구조를 기존과 맞출 수 있다.
def broad_exception_handler(e: Exception):
    """
        400 : VALIDATION
        400 : CANNOT_CHANGE
        401 : UNAUTHORIZED
        401 : TOKEN_EXPIRED
        404 : NOT_FOUND
        405 : METHOD_NOT_ALLOWED
        500 : INTERNAL_SERVER_ERROR
    """
    error_data = {"event": "error_handler"}

    if 'Authorization' in request.headers.keys():
        error_data['access_token'] = {"token": request.headers['Authorization']}

    if isinstance(e, HTTPException):
        # @@TODO httpException이 세분화 되어야 한다.
        if e.code == 404 or e.code == "404":
            error_body = {"errorCode": "NOT_FOUND", "errorMessage": "Cannot find the requested resource."}
            error_code = HTTPStatus.NOT_FOUND
        elif e.code == 405 or e.code == "405":
            error_body = {"errorCode": "METHOD_NOT_ALLOWED",
                          "errorMessage": "The method received in the request-line is known by the origin server but not supported."}
            error_code = HTTPStatus.METHOD_NOT_ALLOWED
        else:
            error_body = {"errorCode": "INTERNAL_SERVER_ERROR",
                          "errorMessage": "This HTTP error is not handled by the server."}
            error_code = HTTPStatus.INTERNAL_SERVER_ERROR
            error_data['internal_error'] = {"error": "{0}".format(e), "trace": ""}
    elif isinstance(e, ValidationError):
        error_body = {"errorCode": "VALIDATION",
                      "errorMessage": "The condition set in the request parameter's was not met."}
        error_code = HTTPStatus.BAD_REQUEST
    elif str(e) == "Validation":
        error_body = {"errorCode": "VALIDATION",
                      "errorMessage": "The condition set in the request parameter's was not met."}
        error_code = HTTPStatus.BAD_REQUEST
    elif str(e) == "NotFound":
        error_body = {"errorCode": "NOT_FOUND", "errorMessage": "Cannot find the requested resource."}
        error_code = HTTPStatus.NOT_FOUND
    elif str(e) == "CannotChange":
        # @@TODO
        # 해당 Exception을 여기서 처리하면 요청은 정상적인 상황에서 요청에 대한 기록을 하기 힘들다.
        error_body = {"errorCode": "CANNOT_CHANGE",
                      "errorMessage": "The receipt cannot be reset.(is_table_resettable is false)"}
        error_code = HTTPStatus.BAD_REQUEST
    elif str(e) == "Unauthorized":
        error_body = {"errorCode": "UNAUTHORIZED", "errorMessage": "Incorrect authentication credentials."}
        error_code = HTTPStatus.UNAUTHORIZED
    elif str(e) == "Expired":
        error_body = {"errorCode": "TOKEN_EXPIRED", "errorMessage": "Session Expired."}
        error_code = HTTPStatus.UNAUTHORIZED
    else:
        error_body = {"errorCode": "INTERNAL_SERVER_ERROR",
                      "errorMessage": "The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application."}
        import traceback
        error_code = HTTPStatus.INTERNAL_SERVER_ERROR
        error_data['error'] = {"error": "{0}".format(e), "trace": traceback.format_exc()}
        print(traceback.format_exc())

    error_data['response'] = {"status": error_code.value, "body": error_body}

    log(error_data)

    return jsonify(error_body), error_code
