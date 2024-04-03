import sqlite3

conn = sqlite3.connect("instituto.db")

conn.execute(
    """
        INSERT INTO ESTUDIANTES(nombre, apellido, fecha_nacimiento)
        VALUES ('Abel','Tesfaye','1998-02-07')         
    """)
'''
conn.execute(
    """
        INSERT INTO CARRERAS(nombre, duracion)
        VALUES ('Licenciatura en Contabilidad',4)         
    """)
'''

# Consultar datos de matriculación INNER JOIN
print("\nMATRICULAS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULAS.fecha 
    FROM MATRICULAS
    JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id 
    JOIN CARRERAS ON MATRICULAS.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)


conn.commit()
conn.close()