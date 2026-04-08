from flask import flash, redirect, url_for

from app.core.exceptions import AppError
from app.core.transactions import run_service


class DeleteRoute:

    def __init__(
        self,
        blueprint,
        services,
        url_param,
        success_message,
        redirect_endpoint,
    ):

        self.bp = blueprint
        self.services = services
        self.url_param = url_param
        self.success_message = success_message
        self.redirect_endpoint = redirect_endpoint

        self.register_routes()

    def register_routes(self):

        @self.bp.post(f"/<int:{self.url_param}>/delete")
        def delete(**kwargs):

            # OBJETO
            obj_id = kwargs[self.url_param]

            # SERVICE
            try:
                run_service(
                    lambda: self.services.delete(obj_id),
                    self.success_message,
                    fk_fields=self.services.fk_fields,
                )
                return redirect(url_for(self.redirect_endpoint))

            except AppError as e:
                flash(str(e), "danger")
                return redirect(url_for(self.redirect_endpoint))
