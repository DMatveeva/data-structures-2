class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        return self.find_node_by_key_recursive(key, self.Root, None)

    def find_node_by_key_recursive(self, key, node, parent):
        if not node:
            bst_find = BSTFind()
            bst_find.Node = parent
            bst_find.NodeHasKey = False
            if parent.NodeKey > key:
                bst_find.ToLeft = True
            return bst_find
        if node.NodeKey == key:
            bst_find = BSTFind()
            bst_find.Node = node
            bst_find.NodeHasKey = True
            return bst_find
        if node.NodeValue > key:
            return self.find_node_by_key_recursive(key, node.LeftChild, node)
        if node.NodeValue < key:
            return self.find_node_by_key_recursive(key, node.RightChild, node)

    def AddKeyValue(self, key, val):
        bst_find = self.FindNodeByKey(key)
        if bst_find.NodeHasKey:
            return False
        new_node = BSTNode(key, val, bst_find.Node)
        if bst_find.ToLeft:
            bst_find.Node.LeftChild = new_node
        else:
            bst_find.Node.RightChild = new_node
        return True

    def FinMinMax(self, FromNode, FindMax):
        if FindMax:
            node = self.find_max_recursive(FromNode, FromNode.Parent)
        else:
            node = self.find_min_recursive(FromNode, FromNode.Parent)
        bst_find = BSTFind()
        bst_find.Node = node
        bst_find.NodeHasKey = True
        return bst_find

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
        if new_node != node_to_delete.RightChild:
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
            min_node = self.FinMinMax(right_child, False).Node
            return min_node

    def update_ex_place_of_new_child(self, min_node):
        right_child_of_min_node = min_node.RightChild
        if right_child_of_min_node:
            min_node_parent = min_node.Parent
            min_node_parent.LeftChild = right_child_of_min_node

    def Count(self):
        count = len(self.GetAllNodes())
        return count


    def GetAllNodes(self):
        all_nodes = []
        self.collect_children_nodes(self.Root, all_nodes)
        return all_nodes

    def collect_children_nodes(self, node, nodes):
        if not node:
            return
        nodes.append(node)
        self.collect_children_nodes(node.LeftChild, nodes)
        self.collect_children_nodes(node.RightChild, nodes)