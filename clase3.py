import mysql.connector

mydb = mysql.connector.connect(
    
    host = "localhost",
    user = "root",
    password = "7138",
    database = "pythondb"

)

mycursor = mydb.cursor()

#CREAR DB
#mycursor.execute("CREATE DATABASE pythondb")

#SHOW DB
'''
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
'''

#Create Table 
#mycursor.execute("Create table clientes (name varchar(255) , direccion varchar(255))")

#show Tables
'''
mycursor.execute("show tables")

for x in mycursor:
    print(x)
'''

#Insert Table 
'''
sql = "insert into clientes (name , direccion) values (%s , %s)"
valor = [
    ('ABC1','ABC1'),
    ('ABC2','ABC2'),
    ('ABC3','ABC3'),
    ('ABC4','ABC4'),
    ('ABC5','ABC5'),
]

mycursor.executemany(sql , valor)

mydb.commit()

print (mycursor.rowcount, "insertados")
'''

#SELECT 
mycursor.execute("SELECT * FROM clientes")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)