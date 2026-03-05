from flask import flash, redirect, url_for

from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.services.delete_student import (
    delete_student as delete_student_service,
)  # SERVICIO
from app.core.exceptions import AppError
from app.extensions import db


@students_bp.post("/<int:student_id>/delete")
def delete_student(student_id):
    try:
        # COMMIT
        delete_student_service(student_id)
        db.session.commit()

        # MENSAJE
        flash("Alumno eliminado correctamente", "success")

    # ERROR
    except AppError as e:
        db.session.rollback()
        flash(str(e), "danger")

    return redirect(url_for("students.home"))
