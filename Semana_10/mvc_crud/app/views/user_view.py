# render_template() es una función  de Flask que
# renderiza un template de Jinja2
from flask import render_template

# la función recibe la lista de usuarios y renderiza la pagina
# "usuarios.html"
def usuarios(usuario):
    return render_template('usuarios.html', users=usuario)

# la función renderiza la pagina "registro.html"
def registro():
    return render_template('registro.html')