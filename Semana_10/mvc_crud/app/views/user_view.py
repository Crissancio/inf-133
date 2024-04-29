# render_template() es una función  de Flask que
# renderiza un template de Jinja2
from flask import render_template

# la función recibe la lista de usuarios y renderiza la pagina
# "usuarios.html"
def usuarios(usuarios):
    return render_template('usuarios.html',users=usuarios, title="Lista de Usuarios")

# la función renderiza la pagina "registro.html"
def registro():
    return render_template('registro.html', title= "Registro de usuarios")

def actualizar(user):
    return render_template("actualizar.html", user=user, title="Actualizar Usuario")
