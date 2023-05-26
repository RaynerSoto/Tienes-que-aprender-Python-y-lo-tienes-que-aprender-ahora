#Ciclos anidados son ciclos que dentro tienen otros ciclos
# Estos ciclos son desde dentro hasta afuera por tanto el ciclo más interno se ejecuta primero

def ciclos_anidados():
    for x in range(3): # Outer for
        for k in range(2): # Inner for
            print(x,k)

ciclos_anidados()