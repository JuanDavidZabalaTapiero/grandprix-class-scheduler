from flask import Blueprint, flash, redirect, render_template, url_for

# EXCEPCIONES
from app.db.exceptions import DatabaseConnectionError

from .exceptions import StudentError

# FORMULARIOS
from .forms import RegisterStudentForm

# SERVICIOS
from .services.create_student import create_student

students_bp = Blueprint("students", __name__)


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
        create_student(form.data)

        flash("Estudiante registrado correctamente", "success")
        return redirect(url_for("students.home"))

    except DatabaseConnectionError as e:
        flash(str(e), "danger")

    except StudentError as e:
        flash(str(e), "danger")

    except Exception:
        flash("Error inesperado del sistema", "danger")

    return redirect(url_for("students.home"))
