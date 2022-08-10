class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):
        a.sort()
        self.generate_recursive(None, a, 0, len(a)-1)

    def generate_recursive(self, parent_node, a, start_index, end_index):
        if end_index == start_index:
            index = end_index
        else:
            index = (end_index + start_index) // 2
        key = a[index]
        node = BSTNode(key, parent_node)
        if parent_node is None:
            self.Root = node
            node.Level = 0
        elif parent_node.NodeKey > key:
            parent_node.LeftChild = node
            node.Level = parent_node.Level + 1
        else:
            parent_node.RightChild = node
            node.Level = parent_node.Level + 1

        if index - 1 >= start_index:
            self.generate_recursive(node, a, start_index, index - 1)
        if index + 1 < end_index:
            self.generate_recursive(node, a, index + 1, end_index)

        return node

    def IsBalanced(self, root_node):
        return self.is_node_balanced(root_node)

    def is_node_balanced(self, node):
        if node is None:
            return True

        if not node.LeftChild and not node.RightChild:
            return True
        if not node.LeftChild:
            self.is_node_balanced(node.RightChild)
        if not node.RightChild:
            self.is_node_balanced(node.LeftChild)

        self.is_node_balanced(node.LeftChild)
        self.is_node_balanced(node.RightChild)

        left_depth = self.get_depth(node.LeftChild)
        right_depth = self.get_depth(node.RightChild)

        if abs(left_depth - right_depth) > 1:
            return False
        return True

    def get_depth(self, node):

        if node.LeftChild is None and node.RightChild is None:
            return node.Level
        if node.LeftChild:
            return self.get_depth(node.LeftChild)
        if node.RightChild:
            return self.get_depth(node.RightChild)

        left_depth = self.get_depth(node.LeftChild)
        right_depth = self.get_depth(node.LeftChild)

        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth

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


