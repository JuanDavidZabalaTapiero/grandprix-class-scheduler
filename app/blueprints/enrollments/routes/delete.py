from app.blueprints.enrollments import enrollments_bp
from app.blueprints.enrollments.services.crud import enrollment_services
from app.core.crud.routes.delete import DeleteRoute

DeleteRoute(
    blueprint=enrollments_bp,
    services=enrollment_services,
    url_param="enrollment_id",
    success_message="Matrícula eliminada correctamente",
    redirect_endpoint="students.home",
)
