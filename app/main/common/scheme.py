from pydantic import BaseModel, validator
from typing import Optional


class Request(BaseModel):
    id: str
    method: str
    path: str
    authorization: Optional[dict] = {}
    body: Optional[dict] = {}
    query_string: Optional[str] = ""


class Response(BaseModel):
    status: str
    body: Optional[dict] = {}


class InternalResult(BaseModel):
    db: Optional[dict] = {}
    api_response: Optional[dict] = {}
    api_request: Optional[dict] = {}


class LogDict(BaseModel):
    event: Optional[str] = ""
    request: Optional[Request] = {}
    response: Optional[Response] = {}
    internal_result: Optional[InternalResult] = {}
    internal_error: Optional[dict] = {}
    internal_function: Optional[dict] = {}
