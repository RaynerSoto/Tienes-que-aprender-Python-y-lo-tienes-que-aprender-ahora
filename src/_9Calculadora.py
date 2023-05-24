#Este ejercicio tiene cosas avanzadas en el curso, pero me apetecía hacerlo de la mejor manera posible
def calculadora(valor = 0,iteration = False):
    print(valor)
    if valor == 0 and iteration == False:
        operando = input('Ingrese el valor\n')
        try:
            operando = float(operando)
            valor += operando
        finally:
            if valor != 0:
                calculadora(valor, True)
            else:
                calculadora(valor,False)
    else:
        operando = input('Ingrese el valor\n')
        try:
            operacion = input(
                'Ingrese la operación \n+:Sumar \n-:Restar \n*:Multiplicar \n/:Dividir\n.:Salir\nOtro:Reinicio\n')
            if operacion == '+':
                valor += float(operando)
                calculadora(valor, True)
            elif operacion == '-':
                valor -= float(operando)
                calculadora(valor, True)
            elif operacion == '*':
                valor *= float(operando)
                calculadora(valor, True)
            elif operacion == '/':
                valor /= float(operando, True)
                calculadora(valor)
            elif operacion == '.':
                pass
            else:
                calculadora()
        finally:
            calculadora(valor,True)
