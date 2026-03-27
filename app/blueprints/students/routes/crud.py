from app.blueprints.students import students_bp
from app.blueprints.students.forms.edit_student_form import EditStudentForm
from app.blueprints.students.forms.register_student_form import RegisterStudentForm
from app.blueprints.students.services.create_student import (
    CreateStudentInput,
    create_student,
)
from app.blueprints.students.services.delete_student import delete_student
from app.blueprints.students.services.get_student import get_student_by_id
from app.blueprints.students.services.update_student import (
    UpdateStudentInput,
    update_student,
)
from app.core.crud.routes.crud import CRUDRoutes

CRUDRoutes(
    blueprint=students_bp,
    create=dict(
        form_class=RegisterStudentForm,
        template="students/form.html",
        service=create_student,
        input_class=CreateStudentInput,
        success_message="Alumno registrado correctamente",
        redirect_endpoint="students.home",
    ),
    update=dict(
        form_class=EditStudentForm,
        template="students/form.html",
        service=update_student,
        input_class=UpdateStudentInput,
        get_object=get_student_by_id,
        url_param="student_id",
        success_message="Alumno actualizado correctamente",
        redirect_endpoint="students.home",
    ),
    delete=dict(
        service=delete_student,
        url_param="student_id",
        success_message="Alumno eliminado correctamente",
        redirect_endpoint="students.home",
    ),
)
