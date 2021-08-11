#python -m pip install mysql-connector-python 
import mysql.connector

mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "7138",
    database = "pythondb"

)
mycursor = mydb.cursor()
#Crera DB
#mycursor.execute("CREATE DATABASE pythondb")

#Ver Bases de datos
'''
mycursor.execute("Show Databases")

for x in mycursor:
    print(x)

'''
#Crear tabla en mysql
#mycursor.execute("Create table clientes (nombre varchar(255), direccion varchar(255))")

#Show tables 
mycursor.execute("show tables")

for x in mycursor:
    print(x)

#Insertar datos en una tabla
'''
sql = "Insert into clientes (nombre , direccion) values (%s , %s)"
val = ("Fernando Jose Paz", "Usac 1")

mycursor.execute(sql , val)

mydb.commit()

print(mycursor.rowcount, "insertados")
'''

#insertar multiples datos x lista de tuplas
'''
sql = "insert into clientes (nombre, direccion) values (%s, %s)"
val = [
    ('Nombre1','Direccion 1'),
    ('Nombre2','Direccion 2'),
    ('Nombre3','Direccion 3'),
    ('Nombre4','Direccion 4'),
    ('Nombre5','Direccion 5'),
    ('Nombre6','Direccion 6'),
    ('Nombre7','Direccion 7'),
    ('Nombre8','Direccion 8'),
    ('Nombre9','Direccion 9'),
    ('Nombre10','Direccion 10')
]
mycursor.executemany(sql , val)
mydb.commit()
print(mycursor.rowcount,"insertados")
'''
#Ver los datos de una tabla
mycursor.execute("select * from clientes")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)