from dataclasses import dataclass

from sqlalchemy.exc import IntegrityError

from app.blueprints.students.db_utils import handle_student_integrity_error
from app.core.crud.services import update_model
from app.db.decorators import handle_db_exceptions
from app.db.models import Student

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
        student = update_model(
            data.student,
            {"document_id": data.document_id, "name": data.name, "phone": data.phone},
        )
        return student

    except IntegrityError as e:
        handle_student_integrity_error(e, data.document_id)
