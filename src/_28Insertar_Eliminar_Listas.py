def listas_insertar_eliminar():
    jugadores_favoritos = ['Lionel Andrés Messi','Cristiano Ronaldo','Thomas Müller','Manuel Neuer','Ousmane Dembéle']
    jugadores_favoritos.insert(1,'Gonzalo Higuaín')
    print(jugadores_favoritos)
    jugadores_favoritos.append('Neymar Junior')
    jugadores_favoritos.append('David Villa')
    print(jugadores_favoritos)
    jugadores_favoritos.remove('Gonzalo Higuaín')
    print(jugadores_favoritos)
    jugadores_favoritos.pop(0)
    print(jugadores_favoritos)
    del jugadores_favoritos[0]
    print(jugadores_favoritos)
    
listas_insertar_eliminar()