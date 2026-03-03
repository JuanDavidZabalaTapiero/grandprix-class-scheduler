import logging
from dataclasses import dataclass

from sqlalchemy.exc import IntegrityError

from app.blueprints.students.exceptions import (
    StudentDocumentAlreadyExists,
    StudentError,
)
from app.db.decorators import handle_db_exceptions
from app.db.models import Student
from app.extensions import db

logger = logging.getLogger(__name__)


# =========================
# INPUT CONTRACT
# =========================


@dataclass
class CreateStudentInput:
    document_id: str
    name: str
    phone: str


# =========================
# SERVICE
# =========================


@handle_db_exceptions
def create_student(data: CreateStudentInput) -> Student:
    try:
        # DATOS
        document_id = data.document_id
        name = data.name
        phone = data.phone

        # REGISTRAR
        student = Student(document_id=document_id, name=name, phone=phone)
        db.session.add(student)
        db.session.flush()

        return student

    except IntegrityError as e:
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
