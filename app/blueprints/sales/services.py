from datetime import datetime, timedelta

from sqlalchemy import func

from app.db.models import Category, Enrollment
from app.extensions import db


def count_sales(start_date, end_date):

    # FORMATEAR END-DATE
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    end_date = end_date + timedelta(days=1)

    # QUERY
    results = (
        db.session.query(
            Category.name.label("category"), func.count(Enrollment.id).label("sales")
        )
        .outerjoin(
            Enrollment,
            (Enrollment.category_id == Category.id)
            & (Enrollment.created_at >= start_date)
            & (Enrollment.created_at <= end_date),
        )
        .group_by(Category.id, Category.name)
        .order_by(Category.id)
        .all()
    )

    return {
        "labels": [row.category for row in results],
        "sales": [row.sales for row in results],
    }
