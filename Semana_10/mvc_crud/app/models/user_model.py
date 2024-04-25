from database import db
# importamos el objeto "db" de el archivo "database.py"

# "db.Model" es una clase base para todos los modelos SQLAlchemy
# Define la clase User que hereda db.Model
class User(db.Model): # Representa la tabla "users" en la base de datos
    __tablename__ = 'users'
    # se definen las columnas de la tabla y su tipo de dato
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    bday = db.Column(db.Date, nullable=False)
    
    # definimos el constructor
    def __init__(self, name, last_name, email, password, bday):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.bday = bday
        
    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    # Consigue a todos los usuarios de la base de datos
    @staticmethod
    def get_all():
        return User.query.all()