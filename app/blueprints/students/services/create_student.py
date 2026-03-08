from dataclasses import dataclass

from sqlalchemy.exc import IntegrityError

from app.blueprints.students.db_utils import handle_student_integrity_error
from app.core.crud.services import create_model
from app.db.models import Student

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


def create_student(data: CreateStudentInput) -> Student:
    try:
        student = create_model(
            Student,
            {"document_id": data.document_id, "name": data.name, "phone": data.phone},
        )
        return student

    except IntegrityError as e:
        handle_student_integrity_error(e, data.document_id)
