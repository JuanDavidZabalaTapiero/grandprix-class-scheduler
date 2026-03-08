from app.blueprints.students.exceptions import StudentNotFound
from app.core.crud.services import get_by_id
from app.db.models.student import Student

# =========================
# SERVICE
# =========================


def get_student_by_id(student_id: int) -> Student:
    student = get_by_id(Student, student_id, StudentNotFound)
    return student
