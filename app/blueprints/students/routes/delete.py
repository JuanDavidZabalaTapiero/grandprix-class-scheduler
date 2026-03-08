from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.services.delete_student import delete_student  # SERVICIO
from app.core.crud.routes.delete import DeleteRoute

DeleteRoute(
    blueprint=students_bp,
    service=delete_student,
    url_param="student_id",
    success_message="Alumno eliminado correctamente",
    redirect_endpoint="students.home",
)
