from sqlalchemy import extract, func, select

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

    def get_students_with_absences(self, year):
        latest_absence = (
            select(
                Enrollment.student_id.label("student_id"),
                func.max(Lesson.date).label("latest_absence_date"),
            )
            .join(Lesson, Lesson.enrollment_id == Enrollment.id)
            .where(
                Lesson.lesson_status_id == ABSENCE_STATUS_ID,
                extract("year", Lesson.date) == year,
            )
            .group_by(Enrollment.student_id)
            .subquery()
        )

        return (
            Student.query.join(
                latest_absence, latest_absence.c.student_id == Student.id
            )
            .order_by(latest_absence.c.latest_absence_date.desc(), Student.name.asc())
            .all()
        )


# =========================
# INSTANCIA
# =========================

student_services = StudentService(
    Student,
    StudentNotFound,
    unique_fields={"document_id": StudentDocumentAlreadyExists},
    fk_fields={"enrollments": StudentHasEnrollments},
)
