import sqlite3
import os

conn = sqlite3.connect("instituto.db")

#Crear tabla de carreras
conn.execute(
    """
    CREATE TABLE CARRERAS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL);
    """
)

#insertar datos de carrera
conn.execute(
    """
    INSERT INTO CARRERAS(nombre,duracion)
    VALUES ('Ingenieria en Sistemas',5)
    """
)
conn.execute(
    """
    INSERT INTO CARRERAS(nombre,duracion)
    VALUES ('Licenciatura en Administracion',4)
    """
)

#consultar datos
print("Carreras:")

cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)
    
#crear tabla de estudiantes

conn.execute(
    """
    CREATE TABLE ESTUDIANTES
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL);
    """
)

#insertar estudiantes a la tabla estudiantes

conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre,apellido,fecha_nacimiento)
    VALUES ('Pedro','Infante','1990-05-15')
    """
)

conn.execute(
    """
    INSERT INTO ESTUDIANTES (nombre,apellido, fecha_nacimiento)
    VALUES ('Kendrick','Lamar','1987-06-17')
    """
)

cursor = conn.execute("SELECT * FROM ESTUDIANTES")
print("\nEstudiantes:")
for row in cursor:
    print(row)
    
#creamos la tabla de matriculacion

conn.execute(
    """
    CREATE TABLE MATRICULACION
    (id INTEGER PRIMARY KEY,
    estudiante_id INTEGER NOT NULL,
    carrera_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
    FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
    """
)

#insertamos valores a la tabla 
conn.execute(
    """
    INSERT INTO MATRICULACION(estudiante_id, carrera_id, fecha)
    VALUES(1, 1, '2024-04-01')
    """
)

conn.execute(
    """
    INSERT INTO MATRICULACION(estudiante_id, carrera_id, fecha)
    VALUES(2, 2, '2023-05-02')
    """
)

conn.execute(
    """
    INSERT INTO MATRICULACION(estudiante_id, carrera_id, fecha)
    VALUES(1, 2, '2018-12-12')
    """
)

#mostramos matriculacion

cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha FROM MATRICULACION
    JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id
    JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
    """
)

print("\nMatriculaciones:")
for row in cursor:
    print(row)
    
print("\nMatriculacion")

cursor = conn.execute("SELECT * FROM MATRICULACION")
for row in cursor:
    print(row)
    
conn.execute(
    """
    UPDATE MATRICULACION
    SET fecha = '2023-05-05'
    WHERE id = 2
    """
)

print("\nMatriculacion")

cursor = conn.execute("SELECT * FROM MATRICULACION")
for row in cursor:
    print(row)
    
conn.execute(
    """
    DELETE FROM MATRICULACION
    WHERE id = 3
    """
)

print("\nMatriculacion")

cursor = conn.execute("SELECT * FROM MATRICULACION")
for row in cursor:
    print(row)
    
conn.close()