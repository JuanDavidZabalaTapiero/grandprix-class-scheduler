from sqlalchemy import select

from app.blueprints.enrollments.exceptions import (
    EnrollmentAlreadyExists,
    EnrollmentNotFound,
)
from app.blueprints.students.services.crud import student_services
from app.core.crud.services.crud import CRUDServices
from app.db.models.enrollment import Enrollment
from app.extensions import db

# =========================
# CLASE (SERVICIOS EXTRA)
# =========================


class EnrollmentService(CRUDServices):

    def exists(self, student_id, category_id):
        return db.session.scalar(
            select(Enrollment).where(
                Enrollment.student_id == student_id,
                Enrollment.category_id == category_id,
            )
        )

    def create(self, data: dict):

        # === VALIDACIÓN ===

        # STUDENT
        student = student_services.get_student_by_document_id(data["student_id"])

        # DUPLICADO
        existing = self.exists(student.id, data["category_id"])
        if existing:
            raise EnrollmentAlreadyExists()

        # === REGISTRO ===
        return super().create(
            {"student_id": student.id, "category_id": data["category_id"]}
        )


# =========================
# INSTANCIA
# =========================

enrollment_services = EnrollmentService(
    Enrollment, not_found_exception=EnrollmentNotFound
)
