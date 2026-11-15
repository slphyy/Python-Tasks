def primeira_ocorrencia(lista, key):
    start_index = 0
    end_index = len(lista)

    while start_index < end_index:
        mid_point = (start_index + end_index) // 2

        if lista[mid_point] < key:
            start_index = mid_point + 1   # too small, discard the left half
        else:
            end_index = mid_point         # could be the answer, keep looking left

    return start_index


def ultima_ocorrencia(lista, key):
    start_index = 0
    end_index = len(lista)

    while start_index < end_index:
        mid_point = (start_index + end_index) // 2

        if lista[mid_point] <= key:
            start_index = mid_point + 1   # key or smaller, look further right
        else:
            end_index = mid_point         # too big, discard the right half

    return start_index - 1                # step back onto the last match


def frequencia(lista, key):
    primeiro = primeira_ocorrencia(lista, key)

    if primeiro == len(lista) or lista[primeiro] != key:
        return 0

    ultimo = ultima_ocorrencia(lista, key)
    return ultimo - primeiro + 1


numeros = [1, 2, 2, 2, 2, 3, 4, 5, 5, 9]
print(frequencia(numeros, 2))
print(frequencia(numeros, 5))
print(frequencia(numeros, 7))