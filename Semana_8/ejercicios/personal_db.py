import sqlite3

conn = sqlite3.connect('personal.db')

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre, fecha_creacion)
    VALUES('Ventas','10-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre, fecha_creacion)
    VALUES('Marketing','11-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS(nombre, nivel,fecha_creacion)
    VALUES('Gerente de Ventas','Senior','10-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS(nombre, nivel,fecha_creacion)
    VALUES('Analista de Marketing','Junior','11-04-2020')
    """
)
conn.execute(
    """
    INSERT INTO CARGOS(nombre, nivel,fecha_creacion)
    VALUES('Representante de Ventas','Junior','12-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres, apellido_paterno,apellido_materno,fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
    VALUES('Juan','Gonzales','Perez','15-05-2023',1,1,'15-05-2020')
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres, apellido_paterno,apellido_materno,fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
    VALUES('Maria','Lopez','Martinez','20-06-2023',2,2,'20-06-2020')
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS(id_empleado,salario, fecha_inicio,fecha_fin)
    VALUES(1, 3000, '04-01-2024', '30-04-2025')
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS(id_empleado,salario, fecha_inicio,fecha_fin)
    VALUES(2, 3500, '07-01-2023', '30-04-2024')
    """
)

conn.execute(
    """
    UPDATE EMPLEADOS
    SET cargo_id = 3
    WHERE id = 2
    """
)
conn.execute(
    """
    UPDATE SALARIOS
    SET salario = 3600
    WHERE id = 2
    """
)
conn.execute(
    """
    DELETE FROM SALARIOS
    WHERE id = 2
    """
)

conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres, apellido_paterno,apellido_materno,fecha_contratacion, departamento_id, cargo_id, fecha_creacion)
    VALUES('Carlos','Sanchez','Rodriguez','09-04-2023',2,3,'09-04-2023')
    """
)

'''conn.execute(
    """
    INSERT INTO SALARIOS(id_empleado,salario, fecha_inicio,fecha_fin)
    VALUES(3, 3500, '05-05-2024', '05-12-2025')
    """
)'''

conn.commit()
conn.close()