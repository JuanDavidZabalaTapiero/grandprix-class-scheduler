from flask import redirect, request, url_for

from app.blueprints.enrollments import enrollments_bp
from app.blueprints.enrollments.services.crud import enrollment_services
from app.core.transactions import run_query, run_service


@enrollments_bp.post("/<int:enrollment_id>/schedule-completed")
def update_schedule_completed(enrollment_id):
    enrollment = run_query(lambda: enrollment_services.get_by_id(enrollment_id))
    schedule_completed = request.form.get("schedule_completed") == "on"

    run_service(
        lambda: enrollment_services.update(
            enrollment, {"schedule_completed": schedule_completed}
        ),
        "Estado del cronograma actualizado correctamente",
    )

    return redirect(url_for("enrollments.home", enrollment_id=enrollment_id))
