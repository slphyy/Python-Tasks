def primeiro_horario_disponivel(slots, key):
    start_index = 0
    end_index = len(slots)

    while start_index < end_index:
        mid_point = (start_index + end_index) // 2

        if slots[mid_point] < key:
            start_index = mid_point + 1   # too early, discard the left half
        else:
            end_index = mid_point         # could be the answer, keep looking left

    return start_index if start_index < len(slots) else -1


slots = ['08:00', '09:30', '14:00', '15:30', '16:00']
print(primeiro_horario_disponivel(slots, '15:00'))  # 3
print(primeiro_horario_disponivel(slots, '16:01'))  # -1