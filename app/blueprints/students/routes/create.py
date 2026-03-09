from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.forms import RegisterStudentForm  # FORM
from app.blueprints.students.services.create_student import (
    CreateStudentInput,
    create_student,
)  # SERVICIO
from app.core.crud.routes.create import CreateRoute

CreateRoute(
    blueprint=students_bp,
    form_class=RegisterStudentForm,
    template="students/form.html",
    service=create_student,
    input_class=CreateStudentInput,
    success_message="Alumno registrado correctamente",
    redirect_endpoint="students.home",
)
