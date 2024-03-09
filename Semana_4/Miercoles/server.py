from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema
#Object Type nos ayuda a definir y restringir que tipos de datos estamos
#manejando, Campos ~~ Clases
#El SCHEMA nos ayuda a definir la estructura global y las operaciones disponibles en el API
class Query(ObjectType):
    hello = String()
    byeBye = String()
    #el resolve debe tener relacion con la solicitud/ruta
    def resolve_hello(root, info):
        return "Hello, World!"
    
    def resolve_byeBye(root, info):
        return "Bye Bye"
    
schema = Schema(query=Query)

class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
        
    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = schema.execute(data["query"])
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()