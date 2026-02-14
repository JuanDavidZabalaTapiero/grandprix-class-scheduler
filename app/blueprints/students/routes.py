import logging

from flask import Blueprint, flash, redirect, render_template, url_for

# EXCEPCIONES
from app.db.exceptions import DatabaseConnectionError

from .exceptions import StudentError

# FORMULARIOS
from .forms import RegisterStudentForm

# SERVICIOS
from .services.create_student import create_student

logger = logging.getLogger(__name__)

students_bp = Blueprint("students", __name__)


# ====================
# RUTAS
# ====================


@students_bp.get("/")
def home():
    return render_template("students/home.html")


# === CREATE ===
@students_bp.get("/register")
def register_student_form():
    form = RegisterStudentForm()

    return render_template("students/register.html", form=form)


@students_bp.post("/register")
def register_student():
    form = RegisterStudentForm()

    # VALIDACIÓN (ERROR)
    if not form.validate_on_submit():
        return render_template(
            "students/register.html", form=form
        )  # RENDERIZAR FORM ACTUALIZADO

    # VALIDACIÓN (OK) -> MANEJAR REGISTRO
    try:
        data = {
            "document_id": form.document_id.data,
            "name": form.name.data,
            "phone": form.phone.data,
        }

        create_student(data)

        flash("Alumno registrado correctamente", "success")

        # VIEW: HOME
        return redirect(url_for("students.home"))

    except DatabaseConnectionError as e:
        flash(str(e), "danger")

    except StudentError as e:
        flash(str(e), "danger")

    except Exception:
        logger.exception("Unexpected error while registering student")
        flash("Error inesperado del sistema. Vuelva a intentar más tarde", "danger")

    # VIEW: REGISTRO + FORM
    return render_template("students/register.html", form=form)
