#Operaciones con cadenas y listas


cadena1 = 'tengo una yama que Yama se llama'  # declara variable
lista1 = ['pera', 'manzana', 'naranja', 'uva']  # declara lista
longitud = len(cadena1)  # 32, devuelve longitud de la cadena
elem = len(lista1)  # 4, devuelve nº elementos de la lista 
cuenta = cadena1.count('yama')  # 1, cuenta apariciones de 'yama'
print(cadena1.find('yama'))  # 10, devuelve posición de búsqueda 

cadena2 = cadena1.join('*****')  # inserta cadena1 entre caracteres
lista1 = cadena1.split(' ')  # divide cadena por separador → lista
tupla1 = cadena1.partition(' ')  # divide cadena por separador → tupla
 
cadena2 = cadena1.replace('yama','cabra',1) # busca/sustituye términos 
numero = 3.14  # asigna número con decimales
cadena3 = str(numero)  # convierte número a cadena
#if cadena1.startswith("tengo"):  # evalúa si comienza por “tengo”
#if cadena1.endswith("llama"):  # evalúa si termina por “llama”
#if cadena1.find("llama") != -1:  # evalúa si contiene “llama”

cadena4 = 'Python'  # asigna una cadena a una variable
print(cadena4[0:4])  # muestra desde la posición 0 a 4: "Pyth"
print(cadena4[1])  # muestra la posición 1: "y"
print(cadena4[:3] + '-' + cadena4[3:])  # muestra "Pyt-hon"
print(cadena4[:-3])  # muestra todo menos las tres últimas: "Pyt"

# declara variable con cadena alfanumérica
cadena5 = "  abc;123  "

# suprime caracteres en blanco (y \t\n\r) por la derecha
print(cadena5.rstrip())  # "  abc;123"

# suprime caracteres en blanco (y \t\n\r) por la izquierda
print(cadena5.lstrip())  # "abc;123  "

# suprime caracteres en blanco (y \t\n\r) por derecha e izquierda 
print(cadena5.strip())  # "abc;123"

# suprime caracteres del argumento por la derecha e izquierda
print(cadena5.strip("123456790; "))  # "abc"

cadena6 = "Mar"   # declara una variable
print(cadena5.upper())   # convierte a mayúsculas: "MAR"
print(cadena5.lower())   # convierte a minúsculas: "mar" 