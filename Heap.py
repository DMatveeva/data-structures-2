class Heap:

    def __init__(self):
        self.HeapArray = []

    def MakeHeap(self, a, depth):
        heap_size = pow(2, depth + 1) - 1
        self.HeapArray = heap_size * [None]
        for element in a:
            if element is not None:
                self.Add(element)

    def GetMax(self):
        root = self.HeapArray[0]
        if root is None:
            return -1
        index_of_last_not_none = self.find_none_index(self.HeapArray) - 1
        self.HeapArray[0] = self.HeapArray[index_of_last_not_none]
        self.HeapArray[index_of_last_not_none] = None

        i = 0
        while i < index_of_last_not_none:
            element = self.HeapArray[i]
            index_of_left_child = 2 * i + 1
            left_child = self.HeapArray[index_of_left_child]
            index_of_right_child = 2 * i + 2
            right_child = self.HeapArray[index_of_right_child]
            if not left_child and not right_child:
                break
            if not left_child and right_child > element:
                self.HeapArray[right_child] = element
                self.HeapArray[i] = right_child
                break
            if not left_child and right_child < element:
                break
            if not right_child and left_child > element:
                self.HeapArray[left_child] = element
                self.HeapArray[i] = left_child
                break
            if not right_child and left_child < element:
                break

            max_of_children = left_child if left_child > right_child else right_child
            index_of_max_of_children = index_of_left_child if left_child > right_child else index_of_right_child
            if max_of_children > element:
                self.HeapArray[i] = max_of_children
                self.HeapArray[index_of_max_of_children] = element
                i = index_of_max_of_children
            else:
                break
        return root

    def find_none_index(self, a):
        i = 0
        while a[i] is not None:
            i += 1
        return i

    def Add(self, key):

        index_of_first_none = self.find_none_index(self.HeapArray)
        self.HeapArray[index_of_first_none] = key
        if index_of_first_none == 0:
            return False
        i = index_of_first_none
        while i > 0:
            element = self.HeapArray[i]
            index_of_parent = (i - 1) // 2
            parent = self.HeapArray[index_of_parent]
            if parent < element:
                self.HeapArray[i] = parent
                self.HeapArray[index_of_parent] = element
                i = index_of_parent
            else:
                break
        return True