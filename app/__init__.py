from flask import Flask
from .extensions import appbuilder, db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")
    db.init_app(app)
    with app.app_context():
        appbuilder.init_app(app, db.session)
        # from app.models import Categoria, Ingrediente
        from app.models.categoria import Categoria
        from app.models.ingrediente import Ingrediente
        print("ANTES:")
        print(db.metadata.tables.keys())
        db.create_all()
        print("DESPUÉS:")
        print(db.metadata.tables.keys())
        from app.views import CategoriaView, IngredienteView
        appbuilder.add_view(
                CategoriaView, 
                "Categorías", 
                icon="fa-folder-open-o", 
                category="Recetas")
        
        appbuilder.add_view(
            IngredienteView, 
            "Ingredientes", 
            icon="fa-lemon-o", 
            category="Recetas")
    return app
