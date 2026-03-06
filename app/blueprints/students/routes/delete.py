from flask import redirect, url_for

from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.services.delete_student import (
    delete_student as delete_student_service,
)  # SERVICIO
from app.core.transactions import run_service


@students_bp.post("/<int:student_id>/delete")
def delete_student(student_id):

    # EJECUTAR SERVICIO
    run_service(
        lambda: delete_student_service(student_id), "Alumno eliminado correctamente"
    )

    return redirect(url_for("students.home"))
