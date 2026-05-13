from datetime import datetime

from flask import render_template, request

from app.blueprints.instructors import instructors_bp
from app.blueprints.instructors.services.crud import instructor_services
from app.blueprints.lessons.utils.paid import instructor_report
from app.core.transactions import run_query


@instructors_bp.route("/payroll", methods=["GET", "POST"])
def payroll():

    instructors = run_query(lambda: instructor_services.get_all_active_instructors())

    # =========================================================
    # VARIABLES VACÍAS
    # =========================================================

    lessons_per_day = []
    night_hours = []
    total_paid_lessons = []

    start_date = None
    end_date = None

    # =========================================================
    # FORM SUBMIT
    # =========================================================

    if request.method == "POST":

        start_date_str = request.form.get("start_date")
        end_date_str = request.form.get("end_date")

        if start_date_str and end_date_str:

            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

            report = instructor_report(start_date, end_date)

            lessons_per_day = report["lessons_per_day"]
            night_hours = report["night_hours"]
            total_paid_lessons = report["total_paid_lessons"]

    # =========================================================
    # TEMPLATE
    # =========================================================

    return render_template(
        "instructors/payroll.html",
        instructors=instructors,
        lessons_per_day=lessons_per_day,
        night_hours=night_hours,
        total_paid_lessons=total_paid_lessons,
        start_date=start_date,
        end_date=end_date,
    )
