from sqlalchemy import select

from app.blueprints.categories.exceptions import CategoryNotFound
from app.blueprints.categories.services.crud import category_services
from app.blueprints.enrollments.exceptions import (
    EnrollmentAlreadyExists,
    EnrollmentNotFound,
)
from app.blueprints.students.exceptions import StudentNotFound
from app.core.crud.services.crud import CRUDServices
from app.db.models.enrollment import Enrollment
from app.db.models.student import Student
from app.extensions import db


class EnrollmentService(CRUDServices):

    def create(self, data: dict):

        # == VALIDACIÓN ==

        # STUDENT
        student = db.session.scalar(
            select(Student).where(Student.document_id == data["student_id"])
        )
        if not student:
            raise StudentNotFound()

        # CATEGORY
        category = category_services.get_by_id(data["category_id"])
        if not category:
            raise CategoryNotFound()

        # DUPLICADO
        existing = db.session.scalar(
            select(Enrollment).where(
                Enrollment.student_id == student.id,
                Enrollment.category_id == data["category_id"],
            )
        )
        if existing:
            raise EnrollmentAlreadyExists()

        # == CREAR ==
        return super().create(
            {"student_id": student.id, "category_id": data["category_id"]}
        )


enrollment_services = EnrollmentService(
    Enrollment, not_found_exception=EnrollmentNotFound
)
