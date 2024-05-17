import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear un nuevo animal
'''url = f"{BASE_URL}/libros"
nuevo_libro = {"titulo": "Juan Salvador Gabiota", "autor": "Richard Bach", "edicion":3,"disponibilidad": True}
response = requests.post(url, json=nuevo_libro, headers=headers)
print("Creando un nuevo animal:")
print(response.json())'''

'''# Crear el segundo animal
libro_2 = {"titulo": "La Divina Comedia", "autor": "Dante L.", "edicion":2 ,"disponibilidad": True}
response = requests.post(url, json=libro_2, headers=headers)
print("\nCreando el segundo animal:")
print(response.json())'''

# Obtener la lista de todos los animales
url = f"{BASE_URL}/libros"
response = requests.get(url, headers=headers)
print("\nLista de animales:")
print(response.json())

# Obtener un animal específico por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/3"
response = requests.get(url, headers=headers)
print("\nDetalles del animal con ID 1:")
print(response.json())

# Actualizar un animal existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/3"
datos_actualizacion = {"titulo": "Salvador Gaviota á", "edicion": 4}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el animal con ID 1:")
print(response.json())

# Eliminar un animal existente por su ID (por ejemplo, ID=1)
'''url = f"{BASE_URL}/libros/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el animal con ID 1:")
if response.status_code == 204:
    print(f"Animal con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")'''