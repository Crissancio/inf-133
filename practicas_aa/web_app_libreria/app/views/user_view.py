from flask import render_template
from flask_login import current_user

def list_users(users):
    return render_template(
        "users.html",
        users=users,
        title="Lista de Usuarios",
        current_user=current_user,
    )

def registro():
    return render_template(
        "register_user.html",
        title="Registro",
        current_user=current_user,
    )

def update_user(user):
    return render_template(
        "editar_user.html",
        current_user=current_user,
        title="Editar Usuario",
        user=user
    )
    
def login():
    return render_template(
        "login_user.html",
        current_user=current_user,
        title="Login",
    )

def perfil(user):
    return render_template(
        "profile_user.html",
        title="Perfil del Usuario",
        current_user=current_user,
        user=user,
    )