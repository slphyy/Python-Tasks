def localizar_ou_inserir(lista_ids, novo_id):
    start_index = 0
    end_index = len(lista_ids)
    
    while start_index < end_index:
        mid_point = (end_index + start_index) // 2
    
        if lista_ids[mid_point] < novo_id:
            start_index = mid_point + 1     # discard the left half
        else:
            end_index = mid_point   
    
    return mid_point if lista_ids[mid_point] == novo_id else lista_ids.append(novo_id)

lista_ids = [10, 20, 30]
print(localizar_ou_inserir(lista_ids, 30))