from sqlalchemy import select

from app.blueprints.students.exceptions import (
    StudentMedicalExamNotFound,
    StudentNoteNotFound,
    StudentNotFound,
)
from app.db.models import Student, StudentMedicalExam, StudentNote, StudentPreference
from app.extensions import db


def _get_student(student_id):
    student = db.session.get(Student, student_id)

    if not student:
        raise StudentNotFound()

    return student


def get_student_details(student_id):
    student = _get_student(student_id)

    medical_exams = db.session.scalars(
        select(StudentMedicalExam)
        .where(StudentMedicalExam.student_id == student_id)
        .order_by(
            StudentMedicalExam.exam_date.desc(),
            StudentMedicalExam.id.desc(),
        )
    ).all()

    notes = db.session.scalars(
        select(StudentNote)
        .where(StudentNote.student_id == student_id)
        .order_by(StudentNote.created_at.desc(), StudentNote.id.desc())
    ).all()

    return {
        "student": student,
        "preference": student.preferences,
        "medical_exams": medical_exams,
        "notes": notes,
    }


def update_student_balance(student_id, has_balance):
    student = _get_student(student_id)
    student.has_balance = bool(has_balance)
    return student


def update_student_preference(student_id, wants_automatic):
    student = _get_student(student_id)

    if student.preferences:
        student.preferences.wants_automatic = bool(wants_automatic)
        return student.preferences

    preference = StudentPreference(
        student_id=student.id,
        wants_automatic=bool(wants_automatic),
    )
    db.session.add(preference)
    return preference


def create_student_medical_exam(student_id, exam_date, expiration_date):
    student = _get_student(student_id)

    medical_exam = StudentMedicalExam(
        student_id=student.id,
        exam_date=exam_date,
        expiration_date=expiration_date,
    )
    db.session.add(medical_exam)
    return medical_exam


def update_student_medical_exam(
    student_id,
    medical_exam_id,
    exam_date,
    expiration_date,
):
    medical_exam = db.session.scalar(
        select(StudentMedicalExam).where(
            StudentMedicalExam.id == medical_exam_id,
            StudentMedicalExam.student_id == student_id,
        )
    )

    if not medical_exam:
        raise StudentMedicalExamNotFound()

    medical_exam.exam_date = exam_date
    medical_exam.expiration_date = expiration_date
    return medical_exam


def create_student_note(student_id, note_text):
    student = _get_student(student_id)

    note = StudentNote(
        student_id=student.id,
        note=note_text,
    )
    db.session.add(note)
    return note


def update_student_note(student_id, note_id, note_text):
    note = db.session.scalar(
        select(StudentNote).where(
            StudentNote.id == note_id,
            StudentNote.student_id == student_id,
        )
    )

    if not note:
        raise StudentNoteNotFound()

    note.note = note_text
    return note
