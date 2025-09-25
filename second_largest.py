def second_largest(arr):
    unique_values = set(arr)
    new_list = list(unique_values)
    new_list.sort()
    return new_list[-2]