from app.blueprints.students.exceptions import StudentNotFound
from app.db.decorators import handle_db_exceptions
from app.db.models.student import Student

# =========================
# SERVICE
# =========================


@handle_db_exceptions
def get_student_by_id(student_id: int) -> Student:
    student = Student.query.get(student_id)

    if not student:
        raise StudentNotFound()

    return student
