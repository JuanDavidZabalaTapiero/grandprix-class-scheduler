from .base import BaseSchema


class LessonStatusSchema(BaseSchema):
    fields = ["name", "show_in_scheduling", "is_default"]
