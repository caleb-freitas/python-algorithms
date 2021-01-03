def insertion_sort(lst):

    for current_index in range(1, len(lst)):
        current_value = lst[current_index]
        sub_index = current_index - 1

        while sub_index >= 0 and lst[sub_index] > current_value:
            lst[sub_index + 1] = lst[sub_index]
            sub_index -= 1

        lst[sub_index + 1] = current_value
    
    return lst


