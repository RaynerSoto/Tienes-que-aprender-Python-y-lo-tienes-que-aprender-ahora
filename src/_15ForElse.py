# Que pasa si buscamos un elementos por ejemplo el 2 en una lista que va hasta un millón y no lo detenemos?
import time

#Este es el mal ejemplo de como hacerlo
def buscar_numero():
    tiempo_ini = time.time()
    for x in range(1000000):
        print(x)
        if x == 2:
            print('Se ha encontrado el número 2')
    tiempo_final = time.time()
    print('El tiempo que se demora fue {}'.format(tiempo_final-tiempo_ini))

'''
Este es el ejemplo bien realizado para poder detener el ciclo, si lo compilas verás cuantos números analiza y cuanto de-
mora
'''
def buscar_numero_good():
    tiempo_ini = time.time()
    for x in range(1000000):
        print(x)
        if x == 2:
            print('Se ha encontrado el número 2')
            break
    tiempo_final = time.time()
    print('El tiempo que se demora fue {}'.format(tiempo_final - tiempo_ini))

'''Ahora que hubiese sucedido de no haberlo encontrado, pues que lo hubiera analizado hasta el final, pero no iba a 
devolver nada para eso es el For-Else. En caso de no cumplirse el break pues automáticamente salta al else para saber
que hacer
'''
def probando_for_else(valor = 180):
    for x in range(100):
        if x == valor:
            print('Encontrado en los elementos del uno al cien')
            break
    else:
        print('No se ha encontrado el elemento')
probando_for_else(180)