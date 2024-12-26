# Ya esta instalado en python 
import sqlite3

# Conexion a la base de datos
conexion = sqlite3.connect("./SQLITE/pruebas.db")

#Consulta
cursor = conexion.cursor()

#CREAR UNA TABLA 
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255), 
    descripcion TEXT, 
    precio int(255)
)""")

#GUARDAR CAMBIOS
conexion.commit()
"""
#AGREGAR DATOS
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion del producto', 550)")
#GUARDAR CAMBIOS
conexion.commit()
"""
#lECTURA DE DATOS
cursor.execute("SELECT * FROM productos WHERE precio >= 100;")
productos = cursor.fetchall()

#Borrar registros 
cursor.execute("DELETE FROM productos")
conexion.commit()


for producto in productos:
    print(producto)
    print("-----")

#impresion por elemento
for producto in productos:
    print("Titulo: ",producto[1])
    print("Descripcion: ",producto[2])
    print("Precio: ",producto[3])
    print("-----")

#Insercion de muchos datos
productos = [
    ("Ordenador potatil", "Buen PC", 700),
    ("Telefono movil", "Buen telefono", 140),
    ("Placa base", "Buen placa", 80),
    ("Tablet 15", "Buena tablet", 250)
]
cursor.executemany("INSERT INTO productos VALUES(null, ?, ?, ?)", productos)
conexion.commit()

# ACTUALIZAR LOS DATOS
cursor.execute("UPDATE productos SET precio=678 WHERE precio = 80")

# Sacar el primer registro
cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)



#Cerrar el fichero
conexion.close()