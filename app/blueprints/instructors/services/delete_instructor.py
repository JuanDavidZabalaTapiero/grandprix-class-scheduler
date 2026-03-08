from app.blueprints.instructors.exceptions import InstructorNotFound
from app.core.crud.services import delete_model, get_by_id
from app.db.models.instructor import Instructor

# =========================
# SERVICE
# =========================


def delete_instructor(instructor_id: int) -> None:
    instructor = get_by_id(Instructor, instructor_id, InstructorNotFound)
    delete_model(instructor)
