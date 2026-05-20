from datetime import datetime

from flask import render_template, request

from app.blueprints.students import students_bp
from app.blueprints.students.services.crud import student_services
from app.core.transactions import run_query


@students_bp.get("/")
def home():
    return render_template("students/home.html")


@students_bp.route("/absences", methods=["GET", "POST"])
def absences():
    # INITIAL DATA
    current_year = datetime.now().year
    year = current_year

    # FORM
    if request.method == "POST":
        year = request.form.get("year")

    # QUERY
    students = run_query(lambda: student_services.get_students_with_absences(year))

    return render_template("students/absences.html", students=students, year=year)
