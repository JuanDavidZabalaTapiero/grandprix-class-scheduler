from app.blueprints.categories.services.crud import category_services
from app.blueprints.enrollments import enrollments_bp
from app.blueprints.enrollments.forms.enrollment_form import EnrollmentForm
from app.blueprints.enrollments.services.crud import enrollment_services
from app.core.crud.routes.create import CreateRoute
from app.schemas.enrollment import EnrollmentSchema

# =========================
# CLASE (CONFIG EXTRA)
# =========================


class EnrollmentCreateRoute(CreateRoute):

    def setup_form(self, form):
        categories = category_services.get_all()

        if not categories:
            form.category_id.choices = [(0, "No hay categorías registradas")]
            form.category_id.render_kw = {"disabled": True}
        else:
            form.category_id.choices = [(c.id, c.name) for c in categories]


# =========================
# CREAR RUTA
# =========================


EnrollmentCreateRoute(
    blueprint=enrollments_bp,
    form=EnrollmentForm,
    template="enrollments/register.html",
    services=enrollment_services,
    schema=EnrollmentSchema,
    success_message="Matrícula registrada correctamente",
    redirect_endpoint="students.home",
)
