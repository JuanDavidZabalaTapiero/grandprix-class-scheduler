from sqlalchemy import extract, func, select
from sqlalchemy.orm import joinedload, selectinload

from app.blueprints.students.exceptions import (
    StudentDocumentAlreadyExists,
    StudentHasEnrollments,
    StudentNotFound,
)
from app.core.constants import ABSENCE_STATUS_ID
from app.core.crud.services.crud import CRUDServices
from app.db.models import Enrollment, Lesson, Student, StudentNote
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

    def get_students_with_pending_enrollments(self):
        pending_condition = Enrollment.schedule_completed.is_(False)

        students = db.session.scalars(
            select(Student)
            .where(Student.enrollments.any(pending_condition))
            .options(
                selectinload(Student.enrollments.and_(pending_condition)).joinedload(
                    Enrollment.category
                ),
                joinedload(Student.preferences),
            )
            .order_by(Student.created_at.asc(), Student.id.asc())
        ).all()

        if not students:
            return []

        student_ids = [student.id for student in students]

        notes = db.session.scalars(
            select(StudentNote)
            .where(StudentNote.student_id.in_(student_ids))
            .order_by(StudentNote.created_at.asc(), StudentNote.id.asc())
        ).all()

        notes_by_student = {}
        for note in notes:
            notes_by_student.setdefault(note.student_id, []).append(note)

        results = []

        for student in students:
            pending_enrollments = sorted(
                student.enrollments,
                key=lambda enrollment: (enrollment.created_at, enrollment.id),
            )
            student_notes = notes_by_student.get(student.id, [])

            results.append(
                {
                    "student": student,
                    "pending_enrollments": pending_enrollments,
                    "notes": student_notes,
                    "wants_automatic": (
                        student.preferences.wants_automatic
                        if student.preferences
                        else False
                    ),
                    "has_balance": student.has_balance,
                }
            )

        return results


# =========================
# INSTANCIA
# =========================

student_services = StudentService(
    Student,
    StudentNotFound,
    unique_fields={"document_id": StudentDocumentAlreadyExists},
    fk_fields={"enrollments": StudentHasEnrollments},
)
