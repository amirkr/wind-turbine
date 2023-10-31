from pymongo import errors as mongo_error

from app.utils.exceptions import DatabaseException

def mongo_exception_handler(func):
    async def inner_function(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except mongo_error.DuplicateKeyError as e:
            raise  DatabaseException(message="mongo DuplicateKeyError", exc=e, status_code=400)
        except mongo_error.PyMongoError as e:
            raise  DatabaseException(message="mongo error", exc=e, status_code=500)

    return inner_function
