from flask import render_template


class ListRoute:
    def __init__(
        self,
        blueprint,
        services,
        template,
        context_name,
    ):
        self.bp = blueprint
        self.services = services
        self.template = template
        self.context_name = context_name

        self.register_routes()

    def register_routes(self):

        @self.bp.get("/")
        def home():
            items = self.services.get_all()

            return render_template(self.template, items=items)
