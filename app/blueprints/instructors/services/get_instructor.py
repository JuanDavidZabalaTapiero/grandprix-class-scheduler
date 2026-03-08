from app.blueprints.instructors.exceptions import InstructorNotFound
from app.core.crud.services import get_all, get_by_id
from app.db.models.instructor import Instructor

# =========================
# SERVICES
# =========================


def get_instructor_by_id(instructor_id: int) -> Instructor:
    instructor = get_by_id(Instructor, instructor_id, InstructorNotFound)
    return instructor


def get_all_instructors():
    instructors = get_all(Instructor)
    return instructors
