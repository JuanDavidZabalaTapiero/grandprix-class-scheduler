from .create import CreateRoute
from .delete import DeleteRoute
from .update import UpdateRoute


class CRUDRoutes:

    def __init__(
        self,
        blueprint,
        *,
        services,
        schema,
        create: dict | None = None,
        update: dict | None = None,
        delete: dict | None = None,
    ):

        self.bp = blueprint
        self.services = services
        self.schema = schema

        # === CREAR RUTAS ===

        if create:
            CreateRoute(
                blueprint=self.bp, services=self.services, schema=self.schema, **create
            )

        if update:
            UpdateRoute(
                blueprint=self.bp, services=self.services, schema=self.schema, **update
            )

        if delete:
            DeleteRoute(blueprint=self.bp, services=self.services, **delete)
