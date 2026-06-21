from flask import Flask
from .extensions import appbuilder, db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")
    db.init_app(app)

    with app.app_context():
        appbuilder.init_app(app, db.session)

        # Importar modelos para que SQLAlchemy los registre
        from app.models.categoria import Categoria
        from app.models.ingrediente import Ingrediente
        from app.models.receta import Receta
        from app.models.receta_ingrediente import RecetaIngrediente

        db.create_all()

        from app.views import CategoriaView, IngredienteView
        #from app.views.receta_view import RecetaView
        from app.views.receta_view import RecetaView, RecetaIngredienteView
        from app.views.reportes import ReporteSimpleView
        from app.views.reporte_graficas import ReporteCategoriaView


        appbuilder.add_view(CategoriaView, "Categorías", icon="fa-folder-open-o", category="Recetas")
        appbuilder.add_view(IngredienteView, "Ingredientes", icon="fa-lemon-o", category="Recetas")
        #appbuilder.add_view(RecetaView, "Recetas", icon="fa-lemon-o", category="Recetas")
        appbuilder.add_view_no_menu(RecetaIngredienteView)
        appbuilder.add_view(RecetaView, "Recetas", icon="fa-lemon-o", category="Recetas")
        appbuilder.add_view(ReporteSimpleView, "Reportes de recetas por categoria", icon="fa-lemon-o", category="Reportes")
        appbuilder.add_view(ReporteCategoriaView, "Graficas por categoria", icon="fa-bar-chart", category="Reportes")

    return app