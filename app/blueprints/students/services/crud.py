from sqlalchemy.exc import IntegrityError

from app.blueprints.students.db_utils import handle_student_integrity_error
from app.blueprints.students.exceptions import StudentNotFound
from app.core.crud.services.crud import CRUDServices
from app.db.decorators import handle_db_exceptions
from app.db.models.student import Student


class StudentServices(CRUDServices):

    @handle_db_exceptions
    def create(self, data: dict):
        try:
            return super().create(data)

        except IntegrityError as e:
            handle_student_integrity_error(e, data.get("document_id"))

    @handle_db_exceptions
    def update(self, instance, data: dict):
        try:
            return super().update(instance, data)

        except IntegrityError as e:
            handle_student_integrity_error(e, data.get("document_id"))


student_services = StudentServices(Student, StudentNotFound)
