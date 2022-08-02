class aBST:

    def __init__(self, depth):
        tree_size = pow(2, depth + 1) - 1
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        return self.find_node_by_key_recursive(key, 0)

    def find_node_by_key_recursive(self, key, index):
        if index >= len(self.Tree):
            return None
        value = self.Tree[index]
        if value is None:
            return -index
        if value > key:
            return self.find_node_by_key_recursive(key, 2 * index + 1)
        if value < key:
            return self.find_node_by_key_recursive(key, 2 * index + 2)

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index > 0:
            return index
        if index < 0:
            new_index = -index
            self.Tree[new_index] = key
            return new_index
