# En una casa asumimo que las personas pueden estar tanto en la sala como en el patio como fuera de la casa
def casa_inteligente():
    personas_sala = 0
    personas_patio = 0
    if personas_patio == 0 and personas_sala == 0:
        print('Las personas están fuera de la casa. Apagando')
    elif personas_sala == 0 and personas_patio != 0:
        print('Apagando la sala y encendiendo el patio')
    else:
        print('Apagando el patio y encendiendo la sala')
