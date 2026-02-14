import logging

from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from app.blueprints.students.exceptions import (
    StudentDocumentAlreadyExists,
    StudentError,
)
from app.db.exceptions import DatabaseConnectionError
from app.db.models import Student
from app.extensions import db

# LOGS
logger = logging.getLogger(__name__)


def create_student(data: dict) -> Student:
    try:
        # DATOS
        document_id = data["document_id"]
        name = data["name"]
        phone = data["phone"]

        # REGISTRAR
        student = Student(document_id=document_id, name=name, phone=phone)

        db.session.add(student)
        db.session.commit()

        return student

    except IntegrityError as e:
        db.session.rollback()

        error_code = e.orig.args[0]

        # ERROR: DUPLICATE
        if error_code == 1062:
            logger.warning("Duplicate student attempt | document_id=%s", document_id)
            raise StudentDocumentAlreadyExists() from e

        logger.exception(
            "Unexpected IntegrityError while creating student | document_id=%s",
            document_id,
        )
        raise StudentError() from e

    except OperationalError as e:
        db.session.rollback()
        logger.exception("Database connection error while creating student")
        raise DatabaseConnectionError() from e

    except SQLAlchemyError as e:
        db.session.rollback()
        logger.exception(
            "Unexpected SQLAlchemyError while creating student | document_id=%s",
            document_id,
        )
        raise StudentError() from e
