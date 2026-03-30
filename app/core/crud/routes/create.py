from flask import redirect, url_for

from app.core.exceptions import AppError
from app.core.transactions import run_service

from .base import BaseFormRoute


class CreateRoute(BaseFormRoute):

    action_label = "Registrar"

    def __init__(
        self,
        blueprint,
        form_class,
        template,
        services,
        schema,
        success_message,
        redirect_endpoint,
    ):
        self.bp = blueprint
        self.form_class = form_class
        self.template = template
        self.services = services
        self.schema = schema
        self.success_message = success_message
        self.redirect_endpoint = redirect_endpoint

        self.register_routes()

    def register_routes(self):

        @self.bp.get("/register")
        def register_form():

            # GENERAR FORMULARIO
            form = self.form_class()

            return self._render_form(form)

        @self.bp.post("/register")
        def register():

            # FORM
            form = self.form_class()

            if not form.validate_on_submit():
                return self._render_form(form)

            # DATA
            data = self.schema.load(form.to_dict())

            # SERVICIO
            try:
                run_service(lambda: self.services.create(data), self.success_message)

                return redirect(url_for(self.redirect_endpoint))

            except AppError:
                return self._render_form(form)
