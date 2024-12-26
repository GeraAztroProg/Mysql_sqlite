
# Importacion de los paquetes
import mysql.connector

# conexion a la base de datos
database = mysql.connector.connect(
    # host/usur/password/database
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# Saber que la coneccion es correcta
# print(database)

#Creacion de la base de datos
cursor = database.cursor(buffered=True)
"""
#Creacion consultas }
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

#Comprobar si la base de datos existe 
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
#Crear tablas 
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos( 
    id int(10) auto_increment not null, 
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#Comprobar si la base de datos existe 
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

#Insertar valores a la tabla
#cursor.execute("""
#INSERT INTO vehiculos VALUES(
#    null, 
#   'Opel',
#    'Astra',
#    18500
#)
#""")

#Crear datos de forma masiva
#coches = [
 #   ('Seat', 'Ibiza', 5000),
 #   ('Renault', 'Clio', 15000),
 #   ('Citroen', 'Saxo', 2000),
 #   ('Mercedes', 'Clase C', 35000)
#]

#cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
#Guardar los cambios 
database.commit()


# Realiozar consultas de los datos de bd
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")

result = cursor.fetchall()

print("TODOS MIS COCHES")
print(result)

#dATO}
print("SOLO LA MARCA")
for coche in result:
    print(coche[1], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

#Borrar los datos
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()

print(cursor.rowcount, "borrados!!")

#Actualizar los datos 
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat'")
database.commit()
print(cursor.rowcount, "ACTUALIZADO!!")