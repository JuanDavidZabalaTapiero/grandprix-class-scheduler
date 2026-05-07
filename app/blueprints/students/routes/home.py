from flask import render_template

from app.blueprints.students import students_bp
from app.blueprints.students.services.crud import student_services
from app.core.transactions import run_query


@students_bp.get("/")
def home():
    return render_template("students/home.html")


@students_bp.get("/absences")
def absences():
    students = run_query(lambda: student_services.get_students_with_absences())
    return render_template("students/absences.html", students=students)
