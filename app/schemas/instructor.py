from .base import BaseSchema


class InstructorSchema(BaseSchema):
    fields = ["name", "phone", "contract", "enabled"]
