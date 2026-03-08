from app.blueprints.instructors import instructors_bp  # BLUEPRINT
from app.blueprints.instructors.forms.edit_instructor_form import (
    EditInstructorForm,
)  # FORM
from app.blueprints.instructors.services.get_instructor import get_instructor_by_id
from app.blueprints.instructors.services.update_instructor import (
    UpdateInstructorInput,
    update_instructor,
)  # SERVICIO
from app.core.crud.routes.update import UpdateRoute

UpdateRoute(
    blueprint=instructors_bp,
    form_class=EditInstructorForm,
    template="instructors/edit.html",
    service=update_instructor,
    input_class=UpdateInstructorInput,
    get_object=get_instructor_by_id,
    url_param="instructor_id",
    success_message="Instructor actualizado correctamente",
    redirect_endpoint="instructors.home",
)
