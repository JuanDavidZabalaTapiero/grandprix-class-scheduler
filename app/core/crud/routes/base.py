from flask import render_template


class BaseFormRoute:

    action_label = None

    def _render_form(self, form):
        return render_template(
            self.template,
            form=form,
            action_label=self.action_label,
        )
