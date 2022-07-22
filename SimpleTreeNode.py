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
