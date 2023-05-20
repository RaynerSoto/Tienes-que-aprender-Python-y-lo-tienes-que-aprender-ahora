def trabajo():
    nombre_curso = "Ultimate Python"
    descripcion = """ 
    Curso para ser un programador integral en Python.
    Encontrado en Youtube y estudiado por Rayner Alejandro Soto Martínez
    """
    print(nombre_curso,descripcion)
    print(len(nombre_curso))
    print(len(descripcion))
    print(nombre_curso[0]) #El índice 0
    print(nombre_curso[0:10]) #Entre los indices 0 y 9
    print(nombre_curso[9:]) #A partir del indice 9 en adelante
    print(nombre_curso[:11]) # Hasta el índice 11
    print(nombre_curso[:])
    recorriendo_string(nombre_curso)

def recorriendo_string(cadena):
    for x in cadena:
        print(x)