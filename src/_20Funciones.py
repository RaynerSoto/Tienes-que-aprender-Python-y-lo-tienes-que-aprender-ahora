# Ya me has visto crear funciones, pero ahora fue que lo pusieron en el tutorial
def funcion(): # La palabra reservada def sirve para indicar la creación de funciones
    print('Hola')
funcion() # Este es un llamamiento a la función similar a como lo haríamos con un print

#Desarrollo de una función con parámetros, los parámetros pueden estar predefinidos
def imprimir_nombre(nombre = 'Rayner'):
    print(f'Hola me llamo {nombre}')

imprimir_nombre() #Imprimir con parámetros predefinidos
imprimir_nombre('Alejandro') #Imprimir pasando por parámetros
