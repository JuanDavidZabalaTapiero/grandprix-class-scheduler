from flask import flash
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from app.db.exceptions import (
    DatabaseConnectionError,
    DatabaseOperationError,
)
from app.db.utils import handle_integrity_error
from app.extensions import db

from .exceptions import AppError

# =========================
# CREATE / UPDATE / DELETE
# =========================


def run_service(
    service_func, success_message=None, *, unique_fields=None, fk_fields=None
):
    try:
        result = service_func()

        # COMMIT
        db.session.commit()

        # MENSAJE
        flash(success_message, "success")

        return result

    except IntegrityError as e:
        db.session.rollback()
        handle_integrity_error(e, unique_fields=unique_fields, fk_fields=fk_fields)

    except OperationalError as e:
        db.session.rollback()
        raise DatabaseConnectionError() from e

    except SQLAlchemyError as e:
        db.session.rollback()
        raise DatabaseOperationError() from e

    except AppError:
        db.session.rollback()

        # MANEJO EN RUTA
        raise


# =========================
# READ (GET)
# =========================


def run_query(func):
    try:
        return func()

    except OperationalError as e:
        raise DatabaseConnectionError() from e

    except SQLAlchemyError as e:
        raise DatabaseOperationError() from e
