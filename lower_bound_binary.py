numeros = [10, 20, 30, 40, 50]


def lower_bound(lista, key):
    start_index = 0
    end_index = len(lista)

    while start_index < end_index:
        mid_point = (start_index + end_index) // 2

        if lista[mid_point] < key:
            start_index = mid_point + 1   
        else:
            end_index = mid_point

    return start_index if start_index < len(lista) else -1

print(lower_bound(numeros, 35))  # 3