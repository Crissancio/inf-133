import sqlite3
conn = sqlite3.connect("restaurante.db")

cursor = conn.execute(
    """
    SELECT PLATOS.nombre, MESAS.numero 
    FROM PEDIDOS
    JOIN PLATOS ON PEDIDOS.plato_id = PLATOS.id 
    JOIN MESAS ON PEDIDOS.mesa_id = MESAS.id
    """
)
for row in cursor:
    print(row)

cursor = conn.execute(
    """
    SELECT CARRERAS.nombre, ESTUDIANTES.nombre
    FROM CARRERAS
    LEFT JOIN MATRICULAS ON CARRERAS.id = MATRICULAS.carrera_id
    LEFT JOIN ESTUDIANTES ON MATRICULAS.estudiante_id = ESTUDIANTES.id;
    """
)
for row in cursor:
    print(row)

conn.commit()
conn.close()