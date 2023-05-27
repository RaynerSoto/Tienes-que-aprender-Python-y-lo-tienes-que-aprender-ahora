def funciones_argumentos_multiples(*args): # Función con cantidad de argumentos variables
    suma = 0
    for x in args:
        suma += x
    return suma

def funciones_argumentos_multiples_iter(*args):
    return sum(args) # Función que se ocupa de sumar una lista iterable


print(funciones_argumentos_multiples(1,2,3,4,5,6,7,23))