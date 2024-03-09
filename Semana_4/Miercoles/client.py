import requests

#Definir la consulta GraphQL

query = """
    {
        hello
    }
"""
query1 = """ 
    {
        byeBye
    }
"""

url = 'http://localhost:8000/graphql'

#Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query':query})

response1 = requests.post(url, json={'query':query1})

print(response.text)
print(response1.text)