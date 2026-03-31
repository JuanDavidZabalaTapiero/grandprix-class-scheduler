from app.blueprints.categories import categories_bp
from app.blueprints.categories.forms.category_form import CategoryForm
from app.blueprints.categories.services.crud import category_services
from app.core.crud.routes.crud import CRUDRoutes
from app.schemas.category import CategorySchema

CRUDRoutes(
    blueprint=categories_bp,
    services=category_services,
    schema=CategorySchema,
    form_model=CategoryForm,
    list=dict(
        template="categories/home.html",
        context_name="categories",
    ),
    create=dict(
        template="categories/form.html",
        success_message="Categoría registrada correctamente",
        redirect_endpoint="categories.home",
    ),
    update=dict(
        template="categories/form.html",
        url_param="category_id",
        success_message="Categoría actualizada correctamente",
        redirect_endpoint="categories.home",
    ),
    delete=dict(
        url_param="category_id",
        success_message="Categoría eliminada correctamente",
        redirect_endpoint="categories.home",
    ),
)
