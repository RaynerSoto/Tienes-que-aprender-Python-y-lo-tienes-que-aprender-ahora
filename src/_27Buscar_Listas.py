def metodos_busquedas(jugador = 'Lionel Andrés Messi'):
    jugadores_favoritos = ['Lionel Andrés Messi','Cristiano Ronaldo','Thomas Müller','Manuel Neuer','Ousmane Dembéle']
    if jugador in jugadores_favoritos: #Buscando un elemento exacto en una lista
        print('El jugador se encuentra')
    else:
        print('El jugador no se encuentra')
    print(jugadores_favoritos.index(jugador)) # En caso de no encontrar elemento lanza una excepción
    print(jugadores_favoritos.count(jugador)) # Cuenta la cantidad de veces repetidas que tiene un elemento
metodos_busquedas()