#Ahora voy a imprimir los elevados de 2(la funcion pow)
'''
Notas sobre el While:
El while puede dar ciclos infinitos con demasiada facilidad, ya que si no cambia el valor o no se cumple nunca la
condición de parada el siempre va a ejecutar el ciclo, eso es muy importante.
No autoitera como el for, pero si es muy util para trabajos más sencillos y por lo menos en Python es mucho más sencillo
a mi opinión que el ciclo for
Los else se aplican al igual que el for, en caso de no haber break se ejecutará el else al terminar el ciclo
'''
def prueba_ciclo_while():
    numero = 1 # Aqui inicializamos la variable
    while numero <= 100: # Aqui se analiza las condiciones al igual que el if
        numero *= 2
        print(numero)

prueba_ciclo_while()