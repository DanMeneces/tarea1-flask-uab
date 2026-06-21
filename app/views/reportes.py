from flask import request
from app.extensions import db
from flask_appbuilder import BaseView, expose
from app.models.categoria import Categoria
from app.models.ingrediente import Ingrediente
from app.models.receta import Receta
from app.models.receta_ingrediente import RecetaIngrediente

class ReporteSimpleView(BaseView):

    @expose("/", methods=["GET", "POST"])
    def list(self):
        categorias = db.session.query(Categoria).all()

        categoria_objeto = None
        categoria_id_str = ""

        if request.method == "POST":
            categoria_id_str = request.form.get('cat_id', "")
            if categoria_id_str.isdigit():
                categoria_objeto = db.session.get(Categoria, int(categoria_id_str))

        if categoria_objeto:
            ingredientes = (
                db.session.query(Ingrediente)
                .join(RecetaIngrediente, RecetaIngrediente.ingrediente_id == Ingrediente.id)
                .join(Receta, Receta.id == RecetaIngrediente.receta_id)
                .filter(Receta.categoria_id == categoria_objeto.id)
                .distinct()
                .all()
            )
        else:
            ingredientes = db.session.query(Ingrediente).all()

        return self.render_template(
            "reportes.html",
            categorias=categorias,
            categoria_seleccionada=categoria_objeto,
            id_seleccionado=categoria_id_str,
            ingredientes=ingredientes
        )