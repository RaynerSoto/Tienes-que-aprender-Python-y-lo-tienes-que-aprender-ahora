def listado_funciones():
    jugadores_favoritos = ['Lionel Andrés Messi','Cristiano Ronaldo','Thomas Müller','Manuel Neuer','Ousmane Dembéle']
    print(jugadores_favoritos)
    for x in jugadores_favoritos:
        print(x)
    matrices = [[0,1],[2,3]]
    matrices[0][0] = 2
    print(matrices)
    listado = [0] * 10
    print(listado)
    listado = [0,1] * 10
    print(listado)
    listado_2 = listado + jugadores_favoritos
    print(listado_2)
    listado = list(range(1,11)) # Listado de elementos del 1-10
    print(listado)
    listado = list('Hola Mundo')
    print(listado)

    #Manipulando listas:
    #Imprimir un elemento de la lista en una posición
    print(jugadores_favoritos[0])
    #Sustituir una posición de un elemento
    jugadores_favoritos[2] = 'Raheen Sterling'
    print(jugadores_favoritos)
    #Jugadores entre las posiciones 0 y 3
    print(jugadores_favoritos[0:3])
    print(jugadores_favoritos[::5])
listado_funciones()