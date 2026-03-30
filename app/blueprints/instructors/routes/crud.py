from app.blueprints.instructors import instructors_bp
from app.blueprints.instructors.forms.edit_instructor_form import (
    EditInstructorForm,
)
from app.blueprints.instructors.forms.register_instructor_form import (
    RegisterInstructorForm,
)
from app.blueprints.instructors.schema import InstructorSchema
from app.blueprints.instructors.services.crud import instructor_services
from app.core.crud.routes.crud import CRUDRoutes

CRUDRoutes(
    blueprint=instructors_bp,
    services=instructor_services,
    schema=InstructorSchema,
    create=dict(
        form_class=RegisterInstructorForm,
        template="instructors/form.html",
        success_message="Instructor registrado correctamente",
        redirect_endpoint="instructors.home",
    ),
    update=dict(
        form_class=EditInstructorForm,
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
