from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.libro_model import Libro
from views import libro_view
from utils.decorador import role_required

libro_bp = Blueprint("libro",__name__)

@libro_bp.route("/libros")
@login_required
def list_libros():
    libros = Libro.get_all()
    return libro_view.list_libros(libros)

@libro_bp.route("/libros/create", methods=["GET","POST"])
@login_required
@role_required("admin")
def create_libro():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        edicion = int(request.form["edicion"])
        disponible = (request.form["disponible"])
        disponible = True if disponible=="true" else False
        libro = Libro(titulo=titulo, autor=autor, edicion=edicion, disponible=disponible)
        print(libro)
        libro.save()
        flash("Libro creado exitosamente", "success")
        return redirect(url_for("libro.list_libros"))
    return libro_view.create_libro()

@libro_bp.route("/libros/<int:id>/update", methods=["GET","POST"])
@login_required
@role_required("admin")
def update_libro(id):
    libro = Libro.get_by_id(id)
    if not libro:
        return "Libro no encontrado", 404
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        edicion = int(request.form["edicion"])
        disponible = (request.form["disponible"])
        disponible = True if disponible=="true" else False
        libro.update(titulo=titulo, autor=autor, edicion=edicion, disponible=disponible)
        flash("Libro actualizado exitosamente", "success")
        return  redirect(url_for("libro.list_libros"))
    return libro_view.update_libro(libro)

@libro_bp.route("/libros/<int:id>/delete")
@login_required
@role_required("admin")
def delete_libro(id):
    libro = Libro.get_by_id(id)
    if not libro:
        return "Libro no encontrado", 404
    libro.delete()
    flash("Libro eliminado exitosamente", "success")
    return redirect(url_for("libro.list_libros"))