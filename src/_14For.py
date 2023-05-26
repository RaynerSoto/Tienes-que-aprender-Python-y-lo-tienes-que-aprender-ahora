# El ciclo For se utiliza para realizar diversas iteraciones de búsqueda y movimiento entre listas y  demás
# El ciclo sería siempre el mismo por encima for nombre_variable in elementos iterables
#La variable x tomará los valores que se estén iterando

def prueba_for():
    for x in range(5): # La función range 5 devuelve un listado de números del 0-4
        pass # El comando pass es utilizado para poder dejar vacía funciones o ciclos, sin que de error el programa
    for x in range(5):
        print(x) # Ahora se deben imprimir todos los elementos del 0-4

#Como ejercicio de prueba voy a calcular el promedio de los números que se encuentran entre 0 y 10
def ejercicio_prueba():
    suma = 0
    contador = 0
    for x in range(0,11): #Ahora afirmo un valor inicial y uno final en la función
        print(x)
        suma += x
        contador += 1
    print(suma/contador)

def imprimir_valores():
    for x in range(5):
        print('Hola Mundo ' * x)
imprimir_valores()