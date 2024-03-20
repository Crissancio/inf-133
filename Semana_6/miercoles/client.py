import requests
import json

url = "http://localhost:8000"

response = requests.get(f"{url}/posts")

print(response.text)
print("\t\tPrimera participacion\n")
response = requests.get(f"{url}/post/2")
print(response.text)

new_post = {
    "title": "Mi Experiencia como dev",
    "content": "Este es el contenido de la nueva publicación",
}

ruta_post = url +"/posts"
response = requests.post(ruta_post,data=new_post)

print("------POST-------")
print(response.text)


print("------MOSTRANDO-------")
response = requests.get(f"{url}/posts")

print(response.text)

put_data = {
    "content": "En Progreso",
}
ruta_put = url +"/post/3"
response = requests.put(ruta_put,data=put_data)

print("-------PUT------")
print(response.text)

print("------MOSTRANDO-------")
response = requests.get(f"{url}/posts")

print(response.text)

print("------DELETE-------")
response = requests.delete(f"{url}/post/2")

print(response.text)

print("------MOSTRANDO-------")
response = requests.get(f"{url}/posts")

print(response.text)