from database import db

class Libro(db.Model):
    __tablename__ = "libros"
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    edicion = db.Column(db.Integer, nullable=False)
    disponible = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, titulo, autor, edicion, disponible):
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.disponible = disponible
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Libro.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Libro.query.get(id)
    
    def update(self, titulo=None, autor=None, edicion=None, disponible=None):
            if titulo is not None:
                self.titulo = titulo
            if autor is not None:
                self.autor = autor
            if edicion is not None:
                self.edicion = edicion
            if disponible is not None:
                self.disponible = disponible
            db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()