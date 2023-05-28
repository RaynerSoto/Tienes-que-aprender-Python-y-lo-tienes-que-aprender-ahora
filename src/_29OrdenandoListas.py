def ordenando_listas():
    jugadores_favoritos = ['Lionel Andrés Messi','Cristiano Ronaldo','Thomas Müller','Manuel Neuer','Ousmane Dembéle']
    jugadores_favoritos.sort()
    print(jugadores_favoritos)
    jugadores_favoritos.sort(reverse=True)
    print(jugadores_favoritos)
    print(sorted(jugadores_favoritos))
ordenando_listas()