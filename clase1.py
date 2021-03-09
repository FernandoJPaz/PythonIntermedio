#CLASE METODOS, FUNCIONES Y RECURSIVIDAD

#Defincion de la Funcion 
def my_function():
    print("Hello from a function")
    print("Bye From Function")

#llamar Funcion
my_function()


#Funcion Con Argumentos

def my_function(fname):
  print(fname + "Paz Gonzalez")

my_function("Fernando ")
my_function("Jose")


#funcion ccon dos argumentos
def my_function(fname, lname):
    print("-- Funcion con dos parametros --") 
    print(fname + " " , lname)

my_function("Fernando " , "Paz ")

#Funcion Con Error
#Se omite un parametro 
'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
'''

#*args
#Funcion con Argumentos Arbitrarios
def my_function(*kids):
    print("Funcion con Argumentos arbitrarios")
    print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus" , "Fernando ", "Jose")


#ARgumentos con palabras Clave
def my_function(child3, child2, child1):
    print("--- Inicio Argumentos con palabra Clave")
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child3 = "Linus", child2 = "Tobias")


#Palabras Clave Arbitraria
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Valor de parámetro predeterminado
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Pasar una lista como argumento
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Valores devueltos
def my_function(x):
  return 5 * x

Myvariable = my_function(10)

'''
print(my_function(3))
print(my_function(5))
print(my_function(9))
'''
print("El resultado de la llamada a funcion es: ", Myvariable)

#Recursividad sin retorno
def cuenta_regresiva(numero):
  numero -= 1
  if numero > 0:
    print (numero)
    cuenta_regresiva(numero)
  else:
    print("Boooooooom!")      
  print ("Fin de la función", numero)

cuenta_regresiva(20)

#Recursividad con retorno
def factorial(numero):
    print ("Valor inicial ->",numero)
    if numero > 1:
        numero = numero * factorial(numero -1)
    print ("valor final ->",numero)
    return numero

factorial(5)