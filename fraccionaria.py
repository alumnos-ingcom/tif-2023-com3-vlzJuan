def verificar(numero):
    salida = True
    try:
        int(numero)
    except:
        salida = False
    return salida


def calculadora_fraccionaria():
    print("Calculadora fraccionaria")
    #variables
    nt = 0
    dt = 0
    n2 = 0
    d2 = 0

    #ingresar primer fraccion

    nt = input("ingrese numerador: ")
    while(verificar(nt) != True):
        nt = input("numero incorrecto, reintentar: ")
    nt = int(nt)

    dt = input("ingrese denominador: ")
    while(verificar(dt) != True):
        dt = input("numero incorrecto, reintentar: ")
    dt = int(dt)
    while dt == 0:
        print("Error:El denominador no puede ser 0. Reintente.")
        dt = int(input("Introduzca denominador: "))

    #ingresar operando
    opt = str(input("ingrese el operador: "))

    #seleccionar operacion
    while opt != "=":
        n2 = input("ingrese numerador: ")
        while(verificar(n2) != True):
            n2 = input("numero incorrecto, reintentar: ")
        n2 = int(n2)
        d2 = (input("ingrese denominador: "))
        while(verificar(d2) != True):
            d2 = input("numero incorrecto, reintentar: ")

        d2 = int(d2)
        while d2 == 0:
            print("Error:El denominador no puede ser 0. Reintente.")
            d2 = int(input("Introduzca denominador: "))

        if opt == "+":
            nt = (nt * d2) + (n2 * dt)
            dt = dt * d2
            ans = nt, dt

        elif opt == "-":
            nt = (nt * d2) - (n2 * dt)
            dt = dt * d2
            ans = nt, dt

        elif opt == "x":
            nt = nt * n2
            dt = dt * d2
            ans = nt, dt

        elif opt == "/":
            nt = nt * d2 
            dt = n2 * dt
            ans = nt, dt
        
        else:
            print("Operación no valida, reintente con un operando válido.")
        opt = str(input("Ingresar operación: "))
    print(f"{ans}")