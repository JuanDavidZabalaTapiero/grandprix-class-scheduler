from app.blueprints.students import students_bp  # BLUEPRINT
from app.blueprints.students.forms.edit_student_form import EditStudentForm  # FORM
from app.blueprints.students.services.get_student import get_student_by_id
from app.blueprints.students.services.update_student import (
    UpdateStudentInput,
    update_student,
)  # SERVICIO
from app.core.crud.routes.update import UpdateRoute

UpdateRoute(
    blueprint=students_bp,
    form_class=EditStudentForm,
    template="students/edit.html",
    service=update_student,
    input_class=UpdateStudentInput,
    get_object=get_student_by_id,
    url_param="student_id",
    success_message="Alumno actualizado correctamente",
    redirect_endpoint="students.home",
)
