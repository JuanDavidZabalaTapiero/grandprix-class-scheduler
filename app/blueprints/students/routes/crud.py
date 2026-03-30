from app.blueprints.students import students_bp
from app.blueprints.students.forms.edit_student_form import EditStudentForm
from app.blueprints.students.forms.register_student_form import RegisterStudentForm
from app.blueprints.students.schema import StudentSchema
from app.blueprints.students.services.crud import student_services
from app.core.crud.routes.crud import CRUDRoutes

CRUDRoutes(
    blueprint=students_bp,
    services=student_services,
    schema=StudentSchema,
    create=dict(
        form_class=RegisterStudentForm,
        template="students/form.html",
        success_message="Alumno registrado correctamente",
        redirect_endpoint="students.home",
    ),
    update=dict(
        form_class=EditStudentForm,
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
