numeros = [10, 20, 30, 40, 50]

def lower_bound(lista, key):
    for i, valor in enumerate(lista):
        if valor >= key:
            return i
    return -1

print(lower_bound(numeros, 35))