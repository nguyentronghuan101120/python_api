from pydantic import BaseModel
import typing

class BaseResponseModel(BaseModel):
    statusCode: int = 200
    message: typing.Optional[typing.AnyStr] = None
    data: typing.Optional[typing.Any] = None 

    def to_json(self) -> dict:
        return {
            "status":self.statusCode,
            "message": self.message,
            "data":self.data
        }