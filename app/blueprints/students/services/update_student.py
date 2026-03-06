import logging
from dataclasses import dataclass

from sqlalchemy.exc import IntegrityError

from app.blueprints.students.db_utils import handle_student_integrity_error
from app.db.decorators import handle_db_exceptions
from app.db.models import Student
from app.extensions import db

logger = logging.getLogger(__name__)


# =========================
# INPUT CONTRACT
# =========================


@dataclass
class UpdateStudentInput:
    student: Student
    document_id: str
    name: str
    phone: str


# =========================
# SERVICE
# =========================


@handle_db_exceptions
def update_student(data: UpdateStudentInput) -> Student:
    try:
        # DATOS
        student = data.student
        document_id = data.document_id
        name = data.name
        phone = data.phone

        # ACTUALIZAR
        student.document_id = document_id
        student.name = name
        student.phone = phone
        db.session.flush()

        return student

    except IntegrityError as e:
        handle_student_integrity_error(e, document_id)
