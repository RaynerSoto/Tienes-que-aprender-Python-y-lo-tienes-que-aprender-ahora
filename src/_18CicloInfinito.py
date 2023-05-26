import random
import time


def ciclo_infinito():
    while True: # Esta condición se va a ejecutar siempre y no hay break que lo detenga
        print(random.randint(1,8000))
'''        
Como te podrás dar cuenta este código será ejecutado siempre y nada lo va a detener, menos nosotros mismo de manera 
manual
'''


#Sin embargo este código aunque igual tiene sus complicaciones para detenerse en algún momento se romperá su ciclo
def ciclo_infinito2():
    tiempo_inicial = time.time()
    while True: # Aquí igual siempre se ejecuta la condición, pero hay un break que en algún momento lo detendrá
        valor = random.randint(1,8000)
        print(valor)
        if valor == 7980:
            break
    tiempo_final = time.time()
    print(tiempo_final-tiempo_inicial)

    # Este último en una ejecución me dio 0.09