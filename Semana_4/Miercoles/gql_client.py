import requests

query = """
    {
        estudiantes{
            nombre
        }
    }
"""
query_two = """
    {
        estudiantes{
            nombre
            apellido
        }
    }
"""

url = 'http://localhost:8000/graphql'

#Solicitud POST al servidor GraphQL
response_one = requests.post(url, json={'query':query})

response_two = requests.post(url, json={'query':query_two})

print(response_one.text)
print(response_two.text)