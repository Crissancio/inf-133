from flask import Blueprint, request, redirect, url_for
from datetime import datetime

#importamos la vista de usuario
from views import user_view
#importamos el modelo de Usuario
from models.user_model import User

# instanciamos Blueprint
# Blueprint es un objeto que agrupa rutas y vistas 
user_bp = Blueprint('user', __name__)


@user_bp.route('/users')
def list_users():
    users = User.get_all()
    return user_view.usuarios(users)

# la ruta users esta asociada al registro de usuarios 
@user_bp.route('/users/create', methods=['GET','POST'])
def create_user():
    if request.method == 'POST':
        # obtenemos los datos del formulario
        name = request.form['name']
        last = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        date = request.form['bday']
        date = datetime.strptime(date, '%m-%d-%Y')
        # creamos un usuario y lo guardamos
        user = User(name, last, email, password, date)
        user.save()
        # redirigimos a la vista de usuarios
        return redirect(url_for('user.list_users'))
    # llamamos a la vista de registro
    return user_view.registro()

'''@user_bp.route('/users/<int:id>', methods=['GET'])
def obtener_usuario(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    return user_view.actualizar(user)'''

@user_bp.route('/users/<int:id>/update', methods=['GET','POST'])
def update_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    
    if request.method == 'POST':
        name = request.form['name']
        last = request.form['last']
        email = request.form['email']
        password = request.form['password']
        bday = request.form['bday']
        bday = datetime.strptime(bday, '%m-%d-%Y')
        user.name = name
        user.last_name = last
        user.email = email
        user.password = password
        user.bday = bday
        user.update()
        return redirect(url_for('user.list_users'))
    return user_view.actualizar(user)

@user_bp.route('/user/<int:id>/delete') #methods=['GET']
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    User.delete(user)
    return redirect(url_for('user.list_users'))
