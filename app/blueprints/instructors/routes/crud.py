from app.blueprints.instructors import instructors_bp
from app.blueprints.instructors.forms.instructor_form import InstructorForm
from app.blueprints.instructors.services.crud import instructor_services
from app.core.crud.routes.crud import CRUDRoutes
from app.schemas.instructor import InstructorSchema

CRUDRoutes(
    blueprint=instructors_bp,
    services=instructor_services,
    schema=InstructorSchema,
    form_model=InstructorForm,
    list=dict(
        template="instructors/home.html",
        context_name="instructors",
    ),
    create=dict(
        template="instructors/form.html",
        success_message="Instructor registrado correctamente",
        redirect_endpoint="instructors.home",
    ),
    update=dict(
        template="instructors/form.html",
        url_param="instructor_id",
        success_message="Instructor actualizado correctamente",
        redirect_endpoint="instructors.home",
    ),
    delete=dict(
        url_param="instructor_id",
        success_message="Instructor eliminado correctamente",
        redirect_endpoint="instructors.home",
    ),
)
