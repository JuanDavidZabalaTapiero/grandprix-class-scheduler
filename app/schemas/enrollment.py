from .base import BaseSchema


class EnrollmentSchema(BaseSchema):
    fields = ["student_id", "category_id"]
