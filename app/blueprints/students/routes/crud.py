from app.blueprints.students import students_bp
from app.blueprints.students.forms.student_form import StudentForm
from app.blueprints.students.services.crud import student_services
from app.core.crud.routes.crud import CRUDRoutes
from app.schemas.student import StudentSchema

CRUDRoutes(
    blueprint=students_bp,
    services=student_services,
    schema=StudentSchema,
    form_model=StudentForm,
    create=dict(
        template="students/form.html",
        success_message="Alumno registrado correctamente",
        redirect_endpoint="students.home",
    ),
    update=dict(
        template="students/form.html",
        url_param="student_id",
        success_message="Alumno actualizado correctamente",
        redirect_endpoint="students.home",
    ),
    delete=dict(
        url_param="student_id",
        success_message="Alumno eliminado correctamente",
        redirect_endpoint="students.home",
    ),
)
