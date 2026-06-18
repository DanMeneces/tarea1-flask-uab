from flask import request
from app.extensions import db
from flask_appbuilder import BaseView, expose
from app.models.categoria import Categoria
class ReporteSimpleView(BaseView):
    
    @expose("/", methods =["GET", "POST"])
    def list(self):
        categorias = db.session.query(Categoria).all()
        categoria_seleccionada = request.form.get('cat_id')
        return self.render_template(
            "reportes.html",
            categorias = categorias,
            id_categoria=categoria_seleccionada
        )