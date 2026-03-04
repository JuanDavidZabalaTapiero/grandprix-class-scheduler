import logging
from functools import wraps

from sqlalchemy.exc import OperationalError, SQLAlchemyError

from app.db.exceptions import (
    DatabaseConnectionError,
    DatabaseOperationError,
)

logger = logging.getLogger(__name__)


def handle_db_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except OperationalError as e:
            logger.exception("Database connection error")
            raise DatabaseConnectionError() from e

        except SQLAlchemyError as e:
            logger.exception("Unexpected SQLAlchemy error")
            raise DatabaseOperationError() from e

    return wrapper
