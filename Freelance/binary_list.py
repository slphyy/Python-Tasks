numeros = [20, 21, 22, 23, 24, 25, 26, 27]

def busca_binaria(lista, key):
    found = False
    start_index = 0
    end_index = len(lista) - 1

    while start_index <= end_index:
        mid_point = (end_index + start_index) // 2

        if lista[mid_point] == key:
            print('Found at', mid_point)
            found = True
            break

        if lista[mid_point] > key:
            end_index = mid_point - 1     # discard the right half
        else:
            start_index = mid_point + 1   # discard the left half

    if not found:
        return -1

print(busca_binaria(numeros, 33))