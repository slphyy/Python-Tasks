numeros = [2, 4, 4, 4, 5, 7]

def busca_binaria(lista, key):
    result = -1
    start_index = 0
    end_index = len(lista) - 1

    while start_index <= end_index:
        mid_point = (start_index + end_index) // 2

        if lista[mid_point] == key:
            result = mid_point          
            end_index = mid_point - 1
        elif lista[mid_point] > key:
            end_index = mid_point - 1
        else:
            start_index = mid_point + 1

    return result

print(busca_binaria(numeros, 4))