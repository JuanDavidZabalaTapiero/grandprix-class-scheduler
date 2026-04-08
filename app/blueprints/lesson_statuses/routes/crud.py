from app.blueprints.lesson_statuses import lesson_statuses_bp
from app.blueprints.lesson_statuses.forms.lesson_status_form import LessonStatusForm
from app.blueprints.lesson_statuses.services.crud import lesson_status_services
from app.core.crud.routes.crud import CRUDRoutes
from app.schemas.lesson_status import LessonStatusSchema

CRUDRoutes(
    blueprint=lesson_statuses_bp,
    services=lesson_status_services,
    schema=LessonStatusSchema,
    form_model=LessonStatusForm,
    list=dict(
        template="lesson_statuses/home.html",
        context_name="lesson_statuses",
    ),
    create=dict(
        template="lesson_statuses/form.html",
        success_message="Estado de clase registrado correctamente",
        redirect_endpoint="lesson_statuses.home",
    ),
    update=dict(
        template="lesson_statuses/form.html",
        url_param="lesson_status_id",
        success_message="Estado de clase actualizado correctamente",
        redirect_endpoint="lesson_statuses.home",
    ),
    delete=dict(
        url_param="lesson_status_id",
        success_message="Estado de clase eliminado correctamente",
        redirect_endpoint="lesson_statuses.home",
    ),
)
