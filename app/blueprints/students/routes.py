from flask import Blueprint, redirect, render_template, url_for

# FORMULARIOS
from .forms.register_student_form import RegisterStudentForm

students_bp = Blueprint("students", __name__)


@students_bp.get("/")
def home():
    return render_template("students/home.html")


# == CREATE ==
@students_bp.get("/register")
def register_student_form():
    form = RegisterStudentForm()
    return render_template("students/register.html", form=form)


@students_bp.post("/register")
def register_student():
    form = RegisterStudentForm()

    # VALIDACIÓN
    if not form.validate_on_submit():
        return render_template("students/register.html", form=form)

    return redirect(url_for("students.register_student_form"))
