from sqlalchemy import select

from app.blueprints.students.exceptions import (
    StudentDocumentAlreadyExists,
    StudentHasEnrollments,
    StudentNotFound,
)
from app.core.crud.services.crud import CRUDServices
from app.db.models.student import Student
from app.extensions import db

# =========================
# CLASE (SERVICIOS EXTRA)
# =========================


class StudentService(CRUDServices):

    def get_student_by_document_id(self, document_id):
        student = db.session.scalar(
            select(Student).where(Student.document_id == document_id)
        )
        if not student:
            raise StudentNotFound()
        return student


# =========================
# INSTANCIA
# =========================

student_services = StudentService(
    Student,
    StudentNotFound,
    unique_fields={"document_id": StudentDocumentAlreadyExists},
    fk_fields={"enrollments": StudentHasEnrollments},
)
