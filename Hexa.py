def str_hexa(valor):
    if(valor<10):
        sal = str(valor)
    elif(valor == 10):
        sal = "A"
    elif(valor == 11):
        sal = "B"
    elif(valor == 12):
        sal = "C"
    elif(valor == 13):
        sal = "D"
    elif(valor == 14):
        sal = "E"
    else:
        sal = "F"
    return sal

def c_hexa(coc):
    resto = 0
    resultado = ""

    while coc >= 16:
        resto = coc % 16
        coc = coc // 16
        resultado = str_hexa(resto) + resultado 
    resultado = str_hexa(coc) + resultado 
    print(f"{resultado}")
    return 0