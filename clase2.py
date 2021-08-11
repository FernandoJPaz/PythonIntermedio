#CLASE ARCHIVOS
import json
'''
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing.  The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.
'''

#LECTURA
# \\ Windows
# / Linux
# / Mac OS

ruta = 'C:\\Users\\fher_\\Desktop\\HT2\\Entrada.txt'
#'C:\\Archivo.txt'
ruta1 = 'C:\\Users\\fher_\\Desktop\\Archivo.txt'
archivo = open(ruta, 'r')
#print(archivo.read())

print(archivo.readline())
print(archivo.readline())
print(archivo.readline())

print("------- ------")

#print(archivo.readlines())

print("-------")

for x in archivo:
    print(x)

archivo.close()
print("Fin Lectura")


#ESCRITURA

contenido = "***** Fernando Jose Paz Gonzalez ***** \n"
nueva_ruta = "C://Users//fher_//Desktop//pythonintermedio//ArchivoTest.txt"

archivo = open(nueva_ruta, 'w')
archivo.write(contenido)
archivo.write(contenido)
archivo.write(contenido)
print("Escritura de arhivo Exitosa")
archivo.close



archivo = open(nueva_ruta,"r")
#readline

for linea in archivo.readlines():
    print(linea)
archivo.close()


#METODOS
def get_File(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo

def read_File(archivo):
    contenido = archivo.read()
    return contenido

def Write_File(archivo, texto):
    archivo.write(texto)

#TEST METODOS

arc = get_File("C:\\Users\\fher_\\Desktop\\Archivo.txt","r+")
print(read_File(arc))
Write_File(arc,"--- Fernando Jose Paz Gonzalez 05/19/2021 ---")
print(read_File(arc))



#Convertir Json to py
print("Convertir Json to py")
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


#CONVERTIR PY TO JSON
print("CONVERTIR PY TO JSON")
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#CONVERTIR TODOS LOS DATATYPES DE PY A JSON
print("CONVERTIR TODOS LOS DATATYPES DE PY A JSON")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4 , sort_keys= True))