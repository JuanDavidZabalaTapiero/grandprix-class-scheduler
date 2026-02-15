from flask import render_template

from app.blueprints.students import students_bp  # BLUEPRINT


@students_bp.get("/")
def home():
    return render_template("students/home.html")
