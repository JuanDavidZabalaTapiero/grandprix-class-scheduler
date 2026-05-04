from datetime import date, timedelta

from flask import flash, redirect, render_template, request, url_for

from app.blueprints.instructors import instructors_bp
from app.blueprints.instructors.services.crud import instructor_services
from app.blueprints.instructors.utils.schedule import build_instructor_schedule
from app.core.transactions import run_query
from app.core.utils.time import format_date_spanish


@instructors_bp.route("/schedule", methods=["GET", "POST"])
def schedule_list():

    today = date.today()
    tomorrow = today + timedelta(days=1)

    # POST
    if request.method == "POST":
        date_value = request.form.get("date-input")
        flash("Fecha actualizada", "success")
        return redirect(url_for("instructors.schedule_list", date=date_value))

    # GET
    date_value = request.args.get("date", tomorrow)
    instructors = run_query(lambda: instructor_services.get_all_active_instructors())

    return render_template(
        "instructors/schedule_list.html", date=date_value, instructors=instructors
    )


@instructors_bp.get("/schedule/<int:instructor_id>")
def schedule(instructor_id):

    date = request.args.get("date")
    formatted_date = format_date_spanish(date)

    instructor = run_query(lambda: instructor_services.get_by_id(instructor_id))
    schedule_array = build_instructor_schedule(instructor_id, date)

    return render_template(
        "instructors/schedule.html",
        date=formatted_date,
        instructor=instructor,
        schedule_array=schedule_array,
    )
