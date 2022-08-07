def GenerateBBSTArray(a):
    tree_size = len(a)
    a.sort()
    new_array = [None] * tree_size
    generate_bst(a, new_array)
    return new_array


def generate_bst(old_array, new_array):
    arrays_to_process = [old_array]
    i = 0
    while len(arrays_to_process) > 0:
        a = arrays_to_process.pop(0)
        a_len = len(a)
        index_of_center = a_len // 2
        center = a[index_of_center]
        new_array[i] = center
        i += 1
        if index_of_center > 0:
            arrays_to_process.append(a[:index_of_center])
            arrays_to_process.append(a[index_of_center + 1:])

