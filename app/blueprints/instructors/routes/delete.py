from app.blueprints.instructors import instructors_bp  # BLUEPRINT
from app.blueprints.instructors.services.delete_instructor import (
    delete_instructor,
)  # SERVICIO
from app.core.crud.routes.delete import DeleteRoute

DeleteRoute(
    blueprint=instructors_bp,
    service=delete_instructor,
    url_param="instructor_id",
    success_message="Instructor eliminado correctamente",
    redirect_endpoint="instructors.home",
)
