def desempaquetando_listas():
    jugadores_favoritos = ['Lionel Andrés Messi','Cristiano Ronaldo','Thomas Müller','Manuel Neuer','Ousmane Dembéle',
                           'Raheen Sterling','Kevin De Bruine','Kilian Mbappe','Paulo Dybala','Emiliano Martínez']
    print(jugadores_favoritos[0::2])
    primero,*otros = jugadores_favoritos
    print(primero)
    primero,*otros,ultimo = jugadores_favoritos
    print(primero,ultimo)
desempaquetando_listas()