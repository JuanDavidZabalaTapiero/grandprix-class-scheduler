from .create import CreateRoute
from .delete import DeleteRoute
from .list import ListRoute
from .update import UpdateRoute


class CRUDRoutes:

    def __init__(
        self,
        blueprint,
        *,
        services,
        schema,
        form_model,
        list: dict | None = None,
        create: dict | None = None,
        update: dict | None = None,
        delete: dict | None = None,
    ):

        self.bp = blueprint
        self.services = services
        self.schema = schema

        # === CREAR RUTAS ===

        if list:
            ListRoute(blueprint=self.bp, services=self.services, **list)

        if create:
            CreateRoute(
                blueprint=self.bp,
                services=self.services,
                schema=self.schema,
                form=form_model,
                **create,
            )

        if update:
            UpdateRoute(
                blueprint=self.bp,
                services=self.services,
                schema=self.schema,
                form=form_model,
                **update,
            )

        if delete:
            DeleteRoute(blueprint=self.bp, services=self.services, **delete)
