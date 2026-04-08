from app.blueprints.lesson_types import lesson_types_bp
from app.blueprints.lesson_types.forms.lesson_type_form import LessonTypeForm
from app.blueprints.lesson_types.services.crud import lesson_type_services
from app.core.crud.routes.crud import CRUDRoutes
from app.schemas.lesson_type import LessonTypeSchema

CRUDRoutes(
    blueprint=lesson_types_bp,
    services=lesson_type_services,
    schema=LessonTypeSchema,
    form_model=LessonTypeForm,
    list=dict(
        template="lesson_types/home.html",
        context_name="lesson_types",
    ),
    create=dict(
        template="lesson_types/form.html",
        success_message="Tipo de clase registrada correctamente",
        redirect_endpoint="lesson_types.home",
    ),
    update=dict(
        template="lesson_types/form.html",
        url_param="lesson_type_id",
        success_message="Tipo de clase actualizado correctamente",
        redirect_endpoint="lesson_types.home",
    ),
    delete=dict(
        url_param="lesson_type_id",
        success_message="Tipo de clase eliminado correctamente",
        redirect_endpoint="lesson_types.home",
    ),
)
