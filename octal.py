def c_octal(coc):
    resto = 0
    resultado = ""

    while coc >= 8:
        resto = coc % 8
        coc = coc // 8
        resultado = str(resto) + resultado 
    resultado = str(coc) + resultado 
    print(f"{resultado}")
    return 0
