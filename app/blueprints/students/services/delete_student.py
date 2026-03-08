from app.blueprints.students.exceptions import StudentNotFound
from app.core.crud.services import delete_model, get_by_id
from app.db.models.student import Student

# =========================
# SERVICE
# =========================


def delete_student(student_id: int) -> None:
    student = get_by_id(Student, student_id, StudentNotFound)
    delete_model(student)
