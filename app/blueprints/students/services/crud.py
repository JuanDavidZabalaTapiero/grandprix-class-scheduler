from app.blueprints.students.exceptions import (
    StudentDocumentAlreadyExists,
    StudentHasEnrollments,
    StudentNotFound,
)
from app.core.crud.services.crud import CRUDServices
from app.db.models.student import Student

student_services = CRUDServices(
    Student,
    StudentNotFound,
    unique_fields={"document_id": StudentDocumentAlreadyExists},
    fk_fields={"enrollments": StudentHasEnrollments},
)
