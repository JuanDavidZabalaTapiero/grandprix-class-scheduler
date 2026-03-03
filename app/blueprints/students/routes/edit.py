from flask import render_template

from app.blueprints.students import students_bp  # BLUEPRINT


@students_bp.get("/<int:student_id>/edit")
def edit_student_form(student_id):
    return render_template("students/edit.html")
