def binario(numero):
    if numero == 0:
        return ''
    elif numero == 1:
        return '1'
    else:
        resto = numero % 2
        return binario(numero // 2) + str(resto)

print(binario(35))