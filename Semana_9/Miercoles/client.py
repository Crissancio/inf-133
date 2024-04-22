import requests

url = 'http://localhost:5000/'

ruta = url
response = requests.request(method='GET', url=ruta)

print(response.text)

ruta = url+"saludar?nombre=Pedro"
response = requests.request(method='GET', url=ruta)
print(response.text)

ruta = url+"sumar?num1=5&num2=3"
response = requests.request(method='GET', url=ruta)
print(response.text)

ruta = url+"palindromo?cadena=reconocer"
response = requests.request(method='GET', url=ruta)
print(response.text)

ruta = url+'contar?cadena=exepciones&vocal=e'
response = requests.request(method='GET', url=ruta)
print(response.text)