
def aplica_funcion_lista(funcion, lista):
    '''
    Función que aplica una función a todos los elementos de una lista.

    Parámetros:
        funcion: Es una función.
        lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    '''
    l = []
    for i in lista:
        l.append(funcion(i))
    return l


def cuadrado(n):
    return n * n

print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4, 5 , 6,7 , 8 ,9 ,10]))


def apply_discount(price, discount):
    '''
    Función que aplica un descuento a una cantidad.
    Parámetros:
        price: Es un valor real con el precio al que aplicar el descuento.
        discount: Es el porcentaje a descontar.
    Devuelve:
        El precio final tras aplicar el descuento.
    '''
    return price - price * discount / 100
    
def apply_IVA(price, percentage):
    '''
    Función que aplica un IVA a una cantidad.
    Parámetros:
        price: Es un valor real con el precio al que aplicar el IVA.
        percentage: Es el porcentaje del IVA a aplicar.
    Devuelve:
        El precio final tras aplicar el IVA.
    '''
    return price + price * percentage / 100

def price_basket(basket, function):
    '''
    Función que calcula el precio de una cesta de la compra una vez aplicada una función a los precios iniciales.
    Parámetros:
        basket: Es un diccionario formado por pares precio:descuento.
        function: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.
    Devuelve:
        El precio final de la cesta de la compra una vez aplicada la función sobre los precios iniciales.
    '''
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total

print('El precio de la compra tras aplicar los descuentos es: ', price_basket({1000:20, 500:10, 100:1}, apply_discount))
print('El precio de la compra tras aplicar el IVA es: ', price_basket({1000:20, 500:10, 100:1}, apply_IVA))