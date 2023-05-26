def comparadores():
    #Nota esto siempre será de izquierda a derecha
    print(2 != 3) # 2 no es igual a 3
    print(2 == 3) # 2 es igual a 3
    print(2 >= 3) # 2 es mayor e igual que 3
    print(2 <= 3) # 2 es menor e igual que 3
    print(2 > 3) # 2 es mayor que 3
    print(2 < 3) # 2 es menor que 3
    #Nota: Las comparaciones entre tipos de datos distintos casi siempre será falso por ejemplo
    print(2 == '2') # El primer 2 es un int y el segundo un str por tanto como son distintos será false

'''Si una persona va al cine a ver una película de adultos debe tener 17 años o más y si tiene más de 55 tiene un
descuento
'''

'''
Los if/elif/else se ejecutan secuencialmente empezando por el if, por tanto el orden tiene una importancia fundamental,
por tanto se evalúa la expresión if o elif y si alguna se cumpliera no se cumplierán las demás sentencias
'''
def condicionales():
    edad = 18
    if edad >= 17 :
        print('Usted puede proceder a ver la película')
        if edad >= 55:
            print('Usted tiene un descuento por su edad')
    else:
        print('Usted no puede ver la película')

'''
Los operadores lógicos son aquellos que permiten el desarrollo con una o más condiciones.
Para esto observa el explicacion.md donde te dejo la llamada tabla de la verdad para mejor entendimiento
'''
def condicionales_operadores_logicos():
    edad = 69
    sexo = 'M U J E R'
    if edad > 16 and sexo.lower().replace(' ','') == 'hombre':
        print('Juegas fútbol masculino')
    elif edad > 16 and sexo.lower().replace(' ','') == 'mujer':
        print('Juegas fútbol femenino')
    else:
        print('No juegas futbol')
    print(not True) # Negar el valor de la respuesta

condicionales_operadores_logicos()