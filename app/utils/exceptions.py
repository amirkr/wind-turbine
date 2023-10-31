from logging import Logger

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

class CustomBaseException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int,
        action: str = "generic",
        exc: Exception = None,
        exc_info: bool = True
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.action = action
        self.exc = exc
        self.exc_info = exc_info

class DatabaseException(CustomBaseException):
    def __init__(
        self,
        message: str ="",
        action: str = "",
        status_code: int = 500,
        exc: Exception = None,
        exc_info: bool = True
    ) -> None:
        super().__init__(
            message = message,
            status_code=status_code,
            action=action,
            exc=exc,
            exc_info=exc_info
        )

async def custom_exception_handler(request: Request, exception: CustomBaseException) -> JSONResponse:
    logger = Logger(name=exception.action)

    logger.error(msg=exception.message, exc_info=exception.exc_info)

    return JSONResponse(
        status_code=exception.status_code,
        content=jsonable_encoder({"error": {"info_message": exception.message, "exception": exception.exc}}),
    )
