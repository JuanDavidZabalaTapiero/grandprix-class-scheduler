from app.extensions import db


class StudentMedicalExam(db.Model):
    __tablename__ = "student_medical_exams"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False,
    )
    exam_date = db.Column(db.Date, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)

    student = db.relationship("Student", back_populates="medical_exams")
