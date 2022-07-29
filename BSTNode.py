class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        if not self.Root:
            return None
        return self.find_node_by_key_recursive(key, self.Root, None)

    def find_node_by_key_recursive(self, key, node, parent):
        if not node and parent.NodeKey > key:
            bst_find = BSTFind()
            bst_find.Node = parent
            bst_find.NodeHasKey = False
            bst_find.ToLeft = True
            return bst_find
        if not node and parent.NodeKey < key:
            bst_find = BSTFind()
            bst_find.Node = parent
            bst_find.NodeHasKey = False
            return bst_find
        if node.NodeKey == key:
            bst_find = BSTFind()
            bst_find.Node = node
            bst_find.NodeHasKey = True
            return bst_find
        if node.NodeKey > key:
            return self.find_node_by_key_recursive(key, node.LeftChild, node)
        if node.NodeKey < key:
            return self.find_node_by_key_recursive(key, node.RightChild, node)

    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root = BSTNode(key, val, None)
            return True
        bst_find = self.FindNodeByKey(key)
        if bst_find.NodeHasKey:
            return False
        parent = bst_find.Node
        new_node = BSTNode(key, val, parent)
        if bst_find.ToLeft:
            parent.LeftChild = new_node
        else:
            parent.RightChild = new_node
        return True

    def FinMinMax(self, FromNode, FindMax):
        if FindMax:
            node = self.find_max_recursive(FromNode, FromNode.Parent)
        else:
            node = self.find_min_recursive(FromNode, FromNode.Parent)
        return node

    def find_max_recursive(self, node, parent):
        if not node:
            return parent
        return self.find_max_recursive(node.RightChild, node)

    def find_min_recursive(self, node, parent):
        if not node:
            return parent
        return self.find_min_recursive(node.LeftChild, node)

    def DeleteNodeByKey(self, key):
        bst_find = self.FindNodeByKey(key)
        if not bst_find.NodeHasKey:
            return False
        node_to_delete = bst_find.Node
        left_child = node_to_delete.LeftChild
        right_child = node_to_delete.RightChild
        parent = node_to_delete.Parent
        new_node = self.calc_new_child(left_child, right_child)
        if left_child and right_child:
            self.update_all_dependencies(node_to_delete, left_child, right_child, new_node)
        if new_node:
            new_node.Parent = parent

        if not parent:
            self.Root = new_node
            return True

        is_left_child = node_to_delete.NodeKey < parent.NodeKey
        if is_left_child:
            parent.LeftChild = new_node
        else:
            parent.RightChild = new_node
        return True

    def update_all_dependencies(self, node_to_delete, left_child, right_child, new_node):
        left_child.Parent = new_node
        new_node.LeftChild = left_child

        if new_node == node_to_delete.RightChild:
            return

        # When min node has right child, we set this child at the place of min node.
        if new_node.RightChild:
            self.update_ex_place_of_new_child(new_node)
        else:
            new_node.Parent.LeftChild = None
        new_node.RightChild = right_child
        right_child.Parent = new_node

    def calc_new_child(self, left_child, right_child):
        if not left_child and not right_child:
            return None
        if not left_child and right_child:
            return right_child
        if left_child and not right_child:
            return left_child
        if left_child and right_child:
            min_node = self.FinMinMax(right_child, False)
            return min_node

    @staticmethod
    def update_ex_place_of_new_child(min_node):
        right_child_of_min_node = min_node.RightChild
        if right_child_of_min_node:
            min_node_parent = min_node.Parent
            min_node_parent.LeftChild = right_child_of_min_node

    def Count(self):
        count = len(self.get_all_nodes())
        return count

    def get_all_nodes(self):
        all_nodes = []
        self.deep_pre_order(self.Root, all_nodes)
        return all_nodes

    def WideAllNodes(self):
        all_nodes = [self.Root]
        nodes_to_add = [self.Root.LeftChild, self.Root.RightChild]
        while nodes_to_add:
            node = nodes_to_add.pop(0)
            all_nodes.append(node)
            left_child = node.LeftChild
            right_child = node.RightChild
            if left_child:
                nodes_to_add.append(left_child)
            if right_child:
                nodes_to_add.append(right_child)
        return tuple(all_nodes)

    def DeepAllNodes(self, order):
        all_nodes = []
        if order == 0:
            self.deep_in_order(self.Root, all_nodes)
        if order == 1:
            self.deep_post_order(self.Root, all_nodes)
        if order == 2:
            self.deep_pre_order(self.Root, all_nodes)
        return all_nodes

    def deep_in_order(self, node, nodes):
        if not node:
            return
        self.deep_in_order(node.LeftChild, nodes)
        nodes.append(node)
        self.deep_in_order(node.RightChild, nodes)

    def deep_post_order(self, node, nodes):
        if not node:
            return
        self.deep_post_order(node.LeftChild, nodes)
        self.deep_post_order(node.RightChild, nodes)
        nodes.append(node)

    def deep_pre_order(self, node, nodes):
        if not node:
            return
        nodes.append(node)
        self.deep_pre_order(node.LeftChild, nodes)
        self.deep_pre_order(node.RightChild, nodes)




