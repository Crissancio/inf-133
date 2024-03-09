import requests

url = "http://localhost:8000/"

#GET consulta a la ruta /lista_estudiantes
ruta_get_one = url + "lista_estudiantes"
get_response_one = requests.request(method="GET", url=ruta_get_one)

print(get_response_one.text,"\n")

ruta_buscar = url + "buscar_nombre"
get_name_p = requests.request(method="GET",url=ruta_buscar)    

print(get_name_p.text)
#POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Alcachofa",
    "carrera": "Gastronomía",
}

post_response = requests.request(
    method="POST",
    url=ruta_post,
    json=nuevo_estudiante
)

print(post_response.text)