from app.blueprints.instructors.exceptions import InstructorNotFound
from app.core.crud.services.crud import CRUDServices
from app.db.decorators import handle_db_exceptions
from app.db.models.instructor import Instructor


class InstructorServices(CRUDServices):

    @handle_db_exceptions
    def create(self, data: dict):
        return super().create(data)

    @handle_db_exceptions
    def update(self, instance, data: dict):
        return super().update(instance, data)


instructor_services = InstructorServices(Instructor, InstructorNotFound)
