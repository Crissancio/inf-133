from flask import render_template
from flask_login import current_user

def list_libros(libros):
    return render_template(
        "libros.html",
        libros = libros,
        title="Lista de Animales",
        current_user=current_user,
    )

def create_libro():
    return render_template(
        "create_libro.html",
        current_user = current_user,
        title="Crear Libro"
    )

def update_libro(libro):
    return render_template(
        "edit_libro.html",
        title="Editar Libro",
        libro=libro,
        current_user=current_user
    )