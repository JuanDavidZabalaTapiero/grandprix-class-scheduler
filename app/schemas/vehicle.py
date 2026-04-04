from .base import BaseSchema


class VehicleSchema(BaseSchema):
    fields = ["license_plate", "model", "brand", "type", "enabled"]
