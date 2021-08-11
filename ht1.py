'''
def jugar(intento=1):
    respuesta = input("¿De qué color es una fruta? ")

    if respuesta != "naranja":
        if intento < 3:
            print ("\nFallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento) # Llamada recursiva
        else:
            print ("\nPerdiste!")
    else:
        print ("\nGanaste!")


jugar()
'''


#EJERCICIO 2
'''
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

resultado = factorial(5)
print(resultado)
'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

resultado = fibonacci(7)
print (resultado)
