from .create import CreateRoute
from .delete import DeleteRoute
from .update import UpdateRoute


class CRUDRoutes:

    def __init__(
        self,
        blueprint,
        *,
        create: dict | None = None,
        update: dict | None = None,
        delete: dict | None = None,
    ):

        self.bp = blueprint

        # === CREAR RUTAS ===

        if create:
            CreateRoute(blueprint=self.bp, **create)

        if update:
            UpdateRoute(blueprint=self.bp, **update)

        if delete:
            DeleteRoute(blueprint=self.bp, **delete)
