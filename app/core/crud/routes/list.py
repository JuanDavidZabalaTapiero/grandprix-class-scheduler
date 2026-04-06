from flask import render_template

from app.core.transactions import run_query


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
            items = run_query(lambda: self.services.get_all())
            return render_template(self.template, items=items)
