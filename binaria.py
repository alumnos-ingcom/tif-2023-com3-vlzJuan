def c_bin(coc):
    resto = 0
    resultado = ""

    while coc >= 2:
        resto = coc % 2
        coc = coc // 2
        resultado = str(resto) + resultado 
    resultado = str(coc) + resultado 
    print(f"{resultado}")
    return 0