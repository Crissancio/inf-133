from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse,parse_qs
    
estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    
    def response_handler(self, data, response):
        self.send_response(response)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
        
    def find_student_by_id(self,data,id):
        content_length = int(self.headers["Content-Length"])
        
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        if parsed_path.path == "/estudiante":
            if "nombre" in query_params:
               nombre = query_params["nombre"][0]
               estudiantes_filtrados = [
                   estudiante
                   for estudiante in estudiantes
                   if estudiante["nombre"] == nombre
                ]
               
            elif "apellido" in query_params:
               apellido = query_params["apellido"][0]
               estudiantes_filtrados = [
                   estudiante
                   for estudiante in estudiantes
                   if estudiante["apellido"] == apellido
                ]
            
            elif "carrera" in query_params:
               carrera = query_params["carrera"][0]
               estudiantes_filtrados = [
                   estudiante
                   for estudiante in estudiantes
                   if estudiante["nombre"] == carrera
                ]
            if estudiantes_filtrados != []:
                self.response_handler(estudiantes_filtrados, 200)
            else:
                self.response_handler(estudiantes_filtrados,204)
        else:
            self.response_handler({"Error": "Ruta no existente"},404)

    def do_POST(self):
        if self.path == "/agrega_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.response_handler(estudiantes,201)
    def do_PUT(self):
        if self.path == "/estudiante/":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            id = post_data["id"]
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                estudiante.update(post_data)
                self.response_handler(estudiantes,201)
        else:
            self.response_handler({"Error": "Ruta no existente"},404)
    def do_DELETE(self):
        if self.path == "/eliminar_estudiantes":
            estudiantes.clear()
            self.response_handler(estudiantes,200)
        else:
            self.response_handler({"Error": "Ruta no existente"},404)
    


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()