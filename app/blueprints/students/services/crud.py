from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.blueprints.students.exceptions import (
    StudentDocumentAlreadyExists,
    StudentHasEnrollments,
    StudentNotFound,
)
from app.core.constants import ABSENCE_STATUS_ID
from app.core.crud.services.crud import CRUDServices
from app.db.models import Enrollment, Lesson, Student
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

    def get_students_with_absences(self):
        students = (
            Student.query.join(Student.enrollments)
            .join(Enrollment.lessons)
            .filter(Lesson.lesson_status_id == ABSENCE_STATUS_ID)
            .options(
                joinedload(Student.enrollments)
                .joinedload(Enrollment.lessons)
                .joinedload(Lesson.instructor_vehicle),
                joinedload(Student.enrollments)
                .joinedload(Enrollment.lessons)
                .joinedload(Lesson.lesson_status),
                joinedload(Student.enrollments).joinedload(Enrollment.category),
            )
            .distinct()
            .all()
        )
        return students


# =========================
# INSTANCIA
# =========================

student_services = StudentService(
    Student,
    StudentNotFound,
    unique_fields={"document_id": StudentDocumentAlreadyExists},
    fk_fields={"enrollments": StudentHasEnrollments},
)
