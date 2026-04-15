from .base import BaseSchema


class LessonStatusSchema(BaseSchema):
    fields = ["name", "show_in_schedule", "is_default"]
