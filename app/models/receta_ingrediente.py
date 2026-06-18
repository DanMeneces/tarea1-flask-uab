from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.extensions import db

class RecetaIngrediente (db.Model):
    __tablename__= "receta_ingrediente"
    
    receta_id = Column(Integer,  ForeignKey("receta.id"), primary_key=True)
    ingrediente_id = Column(Integer,  ForeignKey("ingrediente.id"), primary_key=True)
    cantidad =  Column (Float, nullable=False)
    
    receta = relationship("Receta", back_populates="ingredientes")
    ingrediente = relationship("Ingrediente")
    
    def __repr__(self):
        return f"{self.cantidad} de  {self.ingrediente.nombre}"