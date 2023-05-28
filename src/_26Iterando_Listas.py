def recorriendo_listas():
    jugadores_favoritos = ['Lionel Andrés Messi', 'Cristiano Ronaldo', 'Thomas Müller', 'Manuel Neuer',
                           'Ousmane Dembéle',
                           'Raheen Sterling', 'Kevin De Bruine', 'Kilian Mbappe', 'Paulo Dybala', 'Emiliano Martínez']
    for x in jugadores_favoritos:
        print(x)
    #Devuelve una tupla para la revisión
    for x in enumerate(jugadores_favoritos):
        print(x)
    for indice,nombre in enumerate(jugadores_favoritos):
        print(indice,nombre)
recorriendo_listas()