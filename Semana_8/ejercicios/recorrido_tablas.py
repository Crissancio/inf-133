import sqlite3

conn = sqlite3.connect('personal.db')

print("\n 1:")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, SALARIOS.salario
    FROM SALARIOS
    JOIN EMPLEADOS ON SALARIOS.id_empleado = EMPLEADOS.id
    """)
for row in cursor:
    print(row)

print("\n 2:")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre, CARGOS.nombre
    FROM EMPLEADOS
    JOIN CARGOS ON CARGOS.id= EMPLEADOS.cargo_id
    JOIN DEPARTAMENTOS ON DEPARTAMENTOS.id= EMPLEADOS.departamento_id
    """)
for row in cursor:
    print(row)

print("\n 3:")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, DEPARTAMENTOS.nombre, CARGOS.nombre, SALARIOS.salario
    FROM EMPLEADOS
    JOIN CARGOS ON CARGOS.id= EMPLEADOS.cargo_id
    JOIN DEPARTAMENTOS ON DEPARTAMENTOS.id= EMPLEADOS.departamento_id
    JOIN SALARIOS ON SALARIOS.id_empleado = EMPLEADOS.id
    """)
for row in cursor:
    print(row)
