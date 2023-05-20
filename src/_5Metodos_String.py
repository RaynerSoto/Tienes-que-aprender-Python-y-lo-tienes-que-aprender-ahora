def prueba_metodos_String():
    animal = 'Perro Feliz'
    print(animal)
    print(animal.lower()) # Todas las letras en minúsculas
    print(animal.upper()) # Todas las letras en mayúsculas
    print(animal.capitalize()) # Primer letra en minuscula el resto en minuscula
    print(animal.title()) # Primeras letras en minúsculas
    animal = '  Perro Feliz   '
    print(animal.capitalize().strip()) # Eliminar los espacios tanto a la derecha como la izquierda
    print(animal.upper().rstrip()) # Eliminar los espacios a la derecha
    print(animal.lower().lstrip()) # Eliminar los espacios a la izquierda
    print(animal.lstrip().find('F')) # Buscar la posicion de una subcadena, devuelve -1 si no la encuentra
    print(animal.lower().replace('p','hie')) # Reemplazar una subcadena por otra
    print('P' in animal) #Encuentra una subcadena True/False
    print('p' not in animal) #Encuentra una subcadena True/False