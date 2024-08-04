from enum import Enum
from aws_lambda_powertools.utilities.typing import LambdaContext


class Status(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


def handler(event: dict, _: LambdaContext) -> dict:
    msg = event.get("message")
    status = Status.OK
    if msg is None:
        msg = "Not Found"
        status = Status.BAD_REQUEST
    return {"message": msg, "status": status.value}
