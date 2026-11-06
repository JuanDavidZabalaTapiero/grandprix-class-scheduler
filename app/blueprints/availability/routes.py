from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.db.models import AvailabilityBlock, Student, StudentAvailability
from app.extensions import db

from .utils import (
    get_availability_grids,
    get_enabled_availability_blocks,
    build_weekday_rows,
)

availability_bp = Blueprint("availability", __name__, url_prefix="/availability")


@availability_bp.get("/")
def home():
    grids = get_availability_grids()
    return render_template("availability/home.html", grids=grids)


@availability_bp.route("/register", methods=["GET", "POST"])
def register():
    blocks = get_enabled_availability_blocks()
    weekday_rows = build_weekday_rows(blocks)

    if request.method == "POST":
        student_id = request.form.get("student_id", type=int)
        selected_ids = {
            int(value)
            for value in request.form.getlist("availability_block_ids")
            if value.isdigit()
        }

        if not student_id:
            flash("Ingresa un ID de alumno válido.", "danger")
            return render_template(
                "availability/register.html",
                blocks=blocks,
                weekday_rows=weekday_rows,
            )

        student = db.session.get(Student, student_id)
        if student is None:
            flash("No existe un alumno con ese ID.", "danger")
            return render_template(
                "availability/register.html",
                blocks=blocks,
                weekday_rows=weekday_rows,
            )

        enabled_ids = {block.id for block in blocks}
        invalid_ids = selected_ids - enabled_ids

        if invalid_ids:
            flash("La selección incluye bloques no disponibles.", "danger")
            return render_template(
                "availability/register.html",
                blocks=blocks,
                weekday_rows=weekday_rows,
            )

        existing_ids = set(
            db.session.scalars(
                db.select(StudentAvailability.availability_block_id).where(
                    StudentAvailability.student_id == student_id
                )
            ).all()
        )

        new_ids = selected_ids - existing_ids

        db.session.add_all(
            StudentAvailability(
                student_id=student_id,
                availability_block_id=block_id,
            )
            for block_id in new_ids
        )
        db.session.commit()

        flash(f"Disponibilidad guardada para {student.name}.", "success")
        return redirect(url_for("availability.register"))

    return render_template(
        "availability/register.html",
        blocks=blocks,
        weekday_rows=weekday_rows,
    )
