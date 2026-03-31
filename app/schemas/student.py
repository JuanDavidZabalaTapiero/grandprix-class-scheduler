from .base import BaseSchema


class StudentSchema(BaseSchema):
    fields = ["document_id", "name", "phone"]
