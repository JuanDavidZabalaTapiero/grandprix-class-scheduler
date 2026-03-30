from flask import redirect, url_for

from app.core.exceptions import AppError
from app.core.transactions import run_service

from .base import BaseFormRoute


class UpdateRoute(BaseFormRoute):

    action_label = "Actualizar"

    def __init__(
        self,
        blueprint,
        form_class,
        template,
        services,
        schema,
        url_param,
        success_message,
        redirect_endpoint,
    ):

        self.bp = blueprint
        self.form_class = form_class
        self.template = template
        self.services = services
        self.schema = schema
        self.url_param = url_param
        self.success_message = success_message
        self.redirect_endpoint = redirect_endpoint

        self.register_routes()

    def register_routes(self):

        @self.bp.get(f"/<int:{self.url_param}>/edit")
        def edit_form(**kwargs):

            # OBJETO
            obj = self.services.get_by_id(kwargs[self.url_param])

            # FORM
            form = self.form_class(obj=obj)

            return self._render_form(form)

        @self.bp.post(f"/<int:{self.url_param}>/edit")
        def edit(**kwargs):

            # OBJETO
            obj = self.services.get_by_id(kwargs[self.url_param])

            # FORM
            form = self.form_class()

            if not form.validate_on_submit():
                return self._render_form(form)

            # DATA
            data = self.schema.load(form.to_dict())

            # SERVICE
            try:
                run_service(
                    lambda: self.services.update(obj, data), self.success_message
                )

                return redirect(url_for(self.redirect_endpoint))

            except AppError:
                return self._render_form(form)
