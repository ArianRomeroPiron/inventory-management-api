import math

def validar_precio(valor):
    try:
        precio = float(valor)


    except ValueError:
        raise ValueError("El valor no es un numero") from None
    
    if math.isinf(precio) or math.isnan(precio):
        raise ValueError("El valor es infinito, por lo tanto no puede contarse como un precio")
    
    if precio <= 0:
        raise ValueError("el valor es un negativo o cero, por lo tanto no puede contarse como un precio")
    return precio

print(validar_precio("-3"))
