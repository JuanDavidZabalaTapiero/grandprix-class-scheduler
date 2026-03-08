from flask import redirect, render_template, url_for

from app.core.exceptions import AppError
from app.core.transactions import run_service


class UpdateRoute:

    def __init__(
        self,
        blueprint,
        form_class,
        template,
        service,
        input_class,
        get_object,
        url_param,
        success_message,
        redirect_endpoint,
    ):

        self.bp = blueprint
        self.form_class = form_class
        self.template = template
        self.service = service
        self.input_class = input_class
        self.get_object = get_object
        self.url_param = url_param
        self.success_message = success_message
        self.redirect_endpoint = redirect_endpoint

        self.register_routes()

    def register_routes(self):

        @self.bp.get(f"/<int:{self.url_param}>/edit")
        def edit_form(**kwargs):

            # OBJETO
            obj = self.get_object(kwargs[self.url_param])

            # FORM
            form = self.form_class(obj=obj)

            return render_template(self.template, form=form)

        @self.bp.post(f"/<int:{self.url_param}>/edit")
        def edit(**kwargs):

            # OBJETO
            obj = self.get_object(kwargs[self.url_param])

            # FORM
            form = self.form_class()

            if not form.validate_on_submit():
                return render_template(self.template, form=form)

            # DATA
            input_data = self.input_class(obj, **form.to_dict())

            # SERVICE
            try:
                run_service(lambda: self.service(input_data), self.success_message)

                return redirect(url_for(self.redirect_endpoint))

            except AppError:
                return render_template(self.template, form=form)
