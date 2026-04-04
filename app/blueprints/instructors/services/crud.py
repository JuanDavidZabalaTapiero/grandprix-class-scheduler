from app.blueprints.instructors.exceptions import InstructorNotFound
from app.core.crud.services.crud import CRUDServices
from app.db.models.instructor import Instructor

instructor_services = CRUDServices(Instructor, InstructorNotFound)
