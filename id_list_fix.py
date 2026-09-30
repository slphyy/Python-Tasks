def localizar_ou_inserir(lista_ids, novo_id):
    start_index = 0
    end_index = len(lista_ids)

    while start_index < end_index:
        mid_point = (start_index + end_index) // 2

        if lista_ids[mid_point] < novo_id:
            start_index = mid_point + 1
        else:
            end_index = mid_point

    if start_index < len(lista_ids) and lista_ids[start_index] == novo_id:
        return start_index
    else:
        lista_ids.insert(start_index, novo_id)
        return start_index

lista_ids = [10, 20, 30]
print(localizar_ou_inserir(lista_ids, 30))