from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "carrera": "Ingeniería en Sistemas",
        "id": 1,
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        elif self.path  == '/buscar_nombre':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            
            self.send_response(404)
            self.send_header('Content-type')
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no Existente"}).encode('utf-8'))

    def do_POST(self):
        if self.path == '/agrega_estudiantes':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data["id"] = len(estudiantes)+1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type')
            self.end_headers()
            self.wfile.write(json.dumps({"Error":"Ruta no Existente"}).encode('utf-8'))
            
def run_server(port = 8000):
    try:
        server_address = ('',port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'\n\t\tIniciando servidor web en http://localhost:{port}/\n')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n\t\tApagando servidor web\n')
        httpd.socket.close()

if __name__ == "__main__":
    run_server()