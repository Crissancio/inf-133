from flask import Blueprint, request, redirect, url_for
from datetime import datetime

#importamos la vista de usuario
from views import user_view
#importamos el modelo de Usuario
from models.user_model import User

# instanciamos Blueprint
# Blueprint es un objeto que agrupa rutas y vistas 
user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def usuarios():
    users = User.get_all()
    return user_view.usuarios(users)

# la ruta users esta asociada al registro de usuarios 
@user_bp.route('/users', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        # obtenemos los datos del formulario
        name = request.form['name']
        last = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        date = request.form['bday']
        date = datetime.strptime(date, '%m/%d/%Y')
        # creamos un usuario y lo guardamos
        user = User(name, last, email, password, date)
        user.save()
        # redirigimos a la vista de usuarios
        return redirect(url_for('user.usuarios'))
    # llamamos a la vista de registro
    return user_view.registro()
        