def listas():
    jugadores_favoritos = [['Lionel Andrés Messi', 10], ['Cristiano Ronaldo', 7], ['Thomas Müller', 23],
                           ['Manuel Neuer', 1], ['Ousmane Dembéle', 7]]
    nombres = [jugador[0] for jugador in jugadores_favoritos] #Obten en un ciclo los elementos y añade a la nueva lista
    print(nombres)
    nombres = [jugador[0] for jugador in jugadores_favoritos if jugador[1] >=7]
    print(nombres)
    nombre = list(map(lambda el:el[0],jugadores_favoritos))
    print(nombre)
    combo = list(filter(lambda el:el[1]>6,jugadores_favoritos))
    print(combo)

listas()