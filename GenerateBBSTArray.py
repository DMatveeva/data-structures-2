def GenerateBBSTArray(a):
    tree_size = len(a)
    a.sort()
    new_array = [None] * tree_size
    generate_bst_recursive(a, new_array, 0)
    return new_array


def generate_bst_recursive(old_array, new_array, i):
    if i >= len(new_array):
        return
    if len(old_array) == 1:
        new_array[i] = old_array[0]
        return
    if len(old_array) == 0:
        return

    old_len = len(old_array)
    index_of_center = old_len // 2
    center = old_array[index_of_center]
    new_array[i] = center
    # [0 ... index_of_center)
    i += 1
    generate_bst_recursive(old_array[:index_of_center], new_array, i)
    # index_of_center ... old_len
    i += 1
    generate_bst_recursive(old_array[index_of_center + 1:], new_array, i)

