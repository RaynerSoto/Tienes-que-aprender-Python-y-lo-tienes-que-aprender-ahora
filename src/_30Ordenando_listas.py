jugadores_favoritos = [['Lionel Andrés Messi', 10], ['Cristiano Ronaldo', 7], ['Thomas Müller', 23],
                       ['Manuel Neuer', 1], ['Ousmane Dembéle', 7]]
def ordenando_listas():
    print(jugadores_favoritos)
    jugadores_favoritos.sort(key=lambda el:el[1],reverse=False) #Funciones lambda para el ordenamiento
    print(jugadores_favoritos)

def ordena_elemento(elemento):
    return elemento[1]

ordenando_listas()
