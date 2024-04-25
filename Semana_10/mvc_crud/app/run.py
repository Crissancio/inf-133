from flask import Flask
# importamos el controlador de usuarios
from controllers import user_controller
# importamos la base de datos
from database import db

# Inicializa la apliacion de Flask
app = Flask(__name__)

# Configuramos la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa "db" con la app FLASK
db.init_app(app)

# registramos el blueprint de usuarios
app.register_blueprint(user_controller.user_bp)

if __name__== '__main__':
    # Crea las tablas si no existen 
    with app.app_context():
        db.create_all()
    app.run(debug=True)