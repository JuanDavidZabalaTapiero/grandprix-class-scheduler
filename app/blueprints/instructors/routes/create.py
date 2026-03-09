from app.blueprints.instructors import instructors_bp  # BLUEPRINT
from app.blueprints.instructors.forms.register_instructor_form import (
    RegisterInstructorForm,
)  # FORM
from app.blueprints.instructors.services.create_instructor import (
    CreateInstructorInput,
    create_instructor,
)  # SERVICIO
from app.core.crud.routes.create import CreateRoute

CreateRoute(
    blueprint=instructors_bp,
    form_class=RegisterInstructorForm,
    template="instructors/form.html",
    service=create_instructor,
    input_class=CreateInstructorInput,
    success_message="Instructor registrado correctamente",
    redirect_endpoint="instructors.home",
)
