import sqlite3

conn = sqlite3.connect("restaurante.db")

conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT NOT NULL);
    """
)

conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL);
    """
)

conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
    FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
    """
)

conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria)
    VALUES('Pizza',10.99,'Italiana')
    """
)

conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria)
    VALUES('Hamburguesa',8.99,'Americana')
    """
)

conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria)
    VALUES('Sushi',12.99,'Japonesa')
    """
)

conn.execute(
    """
    INSERT INTO PLATOS(nombre, precio, categoria)
    VALUES('Ensalada',6.99,'Vegetariana')
    """
)

cursor = conn.execute("SELECT * FROM PLATOS")
for column in cursor:
    print(column)