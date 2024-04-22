import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple
query_lista = """
    {
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL con parametros
query = """
    {
        estudiantePorId(id: 2){
            nombre
        }
    }
"""

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

query_crear1 = """
mutation {
        crearEstudiante(nombre: "Pedro", apellido: "Gonzales", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

query_crear2 = """
mutation {
        crearEstudiante(nombre: "Alvaro", apellido: "Ramirez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

query_crear3 = """
mutation {
        crearEstudiante(nombre: "Pedro", apellido: "Perez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

response_mutation1 = requests.post(url, json={'query': query_crear1})
print(response_mutation1.text)

response_mutation2 = requests.post(url, json={'query': query_crear2})
print(response_mutation2.text)

response_mutation3 = requests.post(url, json={'query': query_crear3})
print(response_mutation3.text)

query_carrera="""
    {
        estudiantesPorCarrera(carrera: "Arquitectura"){
            id
            nombre
            apellido
        }
    }
"""

response_por_carrera = requests.post(url, json={'query': query_carrera})

print(response_por_carrera.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL para eliminar un estudiante
query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)
'''
# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)'''

query_actualizar = """
mutation {
    updateEstudiante(id:2, carrera:"Antropologia", nombre:"Cristoforo"){
        estudiante {
                id
                nombre
                apellido
                carrera
            }
    }
}
"""

response_update = requests.post(url, json={'query': query_actualizar})

print(response_update.text)