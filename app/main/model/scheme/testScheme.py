from pydantic import BaseModel, validator
from typing import Optional


class testJson(BaseModel):
    user_id: str
