from pydantic import BaseModel
import typing

class BaseResponseModel(BaseModel):
    statusCode: int = 200
    message: str
    data: typing.Any

