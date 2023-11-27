from pydantic import BaseModel
import typing
from flask import jsonify


class BaseResponseModel(BaseModel):
    statusCode: int = 200
    message: typing.Optional[typing.AnyStr] = None
    data: typing.Optional[typing.Any] = None

    def to_json(self) -> dict:
        return {"status": self.statusCode, "message": self.message, "data": self.data}


def response(
    data: typing.Optional[typing.Any] = None,
    message: typing.Optional[typing.AnyStr] = "Success",
    statusCode: int = 200,
) -> jsonify:
    return (
        jsonify(
            BaseResponseModel(
                statusCode=statusCode,
                message=message,
                data=data,
            ).to_json()
        ),
        statusCode,
    )
