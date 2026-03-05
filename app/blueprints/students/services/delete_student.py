from app.db.decorators import handle_db_exceptions
from app.extensions import db

from .get_student import get_student_by_id

# =========================
# SERVICE
# =========================


@handle_db_exceptions
def delete_student(student_id: int) -> None:
    student = get_student_by_id(student_id)
    db.session.delete(student)
    db.session.flush()
