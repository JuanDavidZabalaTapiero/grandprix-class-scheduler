from app.blueprints.instructors import instructors_bp
from app.blueprints.instructors.forms.edit_instructor_form import (
    EditInstructorForm,
)
from app.blueprints.instructors.forms.register_instructor_form import (
    RegisterInstructorForm,
)
from app.blueprints.instructors.services.create_instructor import (
    CreateInstructorInput,
    create_instructor,
)
from app.blueprints.instructors.services.delete_instructor import (
    delete_instructor,
)
from app.blueprints.instructors.services.get_instructor import get_instructor_by_id
from app.blueprints.instructors.services.update_instructor import (
    UpdateInstructorInput,
    update_instructor,
)
from app.core.crud.routes.crud import CRUDRoutes

CRUDRoutes(
    blueprint=instructors_bp,
    create=dict(
        form_class=RegisterInstructorForm,
        template="instructors/form.html",
        service=create_instructor,
        input_class=CreateInstructorInput,
        success_message="Instructor registrado correctamente",
        redirect_endpoint="instructors.home",
    ),
    update=dict(
        form_class=EditInstructorForm,
        template="instructors/form.html",
        service=update_instructor,
        input_class=UpdateInstructorInput,
        get_object=get_instructor_by_id,
        url_param="instructor_id",
        success_message="Instructor actualizado correctamente",
        redirect_endpoint="instructors.home",
    ),
    delete=dict(
        service=delete_instructor,
        url_param="instructor_id",
        success_message="Instructor eliminado correctamente",
        redirect_endpoint="instructors.home",
    ),
)
