class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.level = 0


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        parent = NodeToDelete.Parent
        parent.Children.remove(NodeToDelete)

    def GetAllNodes(self):
        all_nodes = []
        self.collect_children_nodes(self.Root, all_nodes)
        return all_nodes

    def collect_children_nodes(self, node, nodes):
        if not node:
            return
        nodes.append(node)
        for child in node.Children:
            self.collect_children_nodes(child, nodes)

    def FindNodesByValue(self, val):
        found_nodes = []
        self.find_nodes(val, self.Root, found_nodes)
        return found_nodes

    def find_nodes(self, val, node, nodes):
        if not node:
            return
        if node.NodeValue == val:
            nodes.append(node)
        for child in node.Children:
            self.find_nodes(val, child, nodes)


    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        all_nodes = self.GetAllNodes()
        nodes_count = len(all_nodes)
        return nodes_count

    def LeafCount(self):
        all_nodes = self.GetAllNodes()
        leaves = []
        for node in all_nodes:
            if len(node.Children) == 0:
                leaves.append(node)
        return len(leaves)

    def set_levels(self):
        self.set_level_recursive(self.Root, 1)

    def set_level_recursive(self, node, level):
        if not node:
            return
        node.level = level
        level += 1
        for child in node.Children:
            self.set_level_recursive(child, level)

    def EvenTrees(self):
        indices_of_vertex = []
        matrix = [row[:] for row in self.m_adjacency]

        y = 0
        while y < self.max_vertex:
            x = y + 1
            while x < self.max_vertex:
                if matrix[y][x] == 0:
                    x += 1
                    continue
                matrix[y][x] = 0
                matrix[x][y] = 0
                supposed_tree = [y]
                self.create_subtree_recursive(x, supposed_tree, matrix)
                if len(supposed_tree) % 2 == 0:
                    indices_of_vertex.append(y)
                    indices_of_vertex.append(x)
                else:
                    matrix[y][x] = 1
                    matrix[x][y] = 1
                x += 1
            y += 1
        vertex_to_break = []
        i = 0
        while i < len(indices_of_vertex):
            index_of_vertex = indices_of_vertex[i]
            vertex_to_break.append(self.vertex[index_of_vertex])
            i += 1
        return vertex_to_break

    def create_subtree_recursive(self, vertex_index, tree, matrix):
        child_index = vertex_index + 1
        while child_index < self.max_vertex:
            e = matrix[vertex_index][child_index]
            if e == 1:
                tree.append(child_index)
                self.create_subtree_recursive(child_index, tree, matrix)
            child_index += 1
