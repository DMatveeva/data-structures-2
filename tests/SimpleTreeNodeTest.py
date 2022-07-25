import unittest

from SimpleTreeNode import SimpleTreeNode, SimpleTree


class MyTestCase(unittest.TestCase):
    def test_add_child_0(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(2, None)
        tree.AddChild(root, node1)
        result = '[1,None][2,1]'
        self.assertEqual(self.get_string_for_tree(tree), result)  # add assertion here

    def test_add_child_1(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(2, None)
        node2 = SimpleTreeNode(3, None)
        tree.AddChild(root, node1)
        tree.AddChild(node1, node2)
        result = '[1,None][2,1][3,2]'
        self.assertEqual(self.get_string_for_tree(tree), result)  # add assertion here

    def test_add_child_2(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(2, None)
        node2 = SimpleTreeNode(3, None)
        tree.AddChild(root, node1)
        tree.AddChild(root, node2)
        result = '[1,None][2,1][3,1]'
        self.assertEqual(self.get_string_for_tree(tree), result)  # add assertion here

    def test_delete_node(self):
        root = SimpleTreeNode(1, None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode(2, None)
        node2 = SimpleTreeNode(3, None)
        tree.AddChild(root, node1)
        tree.AddChild(root, node2)
        tree.DeleteNode(node1)
        result = '[1,None][3,1]'
        self.assertEqual(self.get_string_for_tree(tree), result)  # add assertion here

    def test_find_nodes(self):
        root = SimpleTreeNode('root', None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode('node1', None)
        node2 = SimpleTreeNode('node2', None)
        node3 = SimpleTreeNode('node2', None)
        tree.AddChild(root, node1)
        tree.AddChild(root, node2)
        tree.AddChild(node2, node3)
        result = '[node2,root][node2,node2]'
        test = tree.FindNodesByValue('node2')
        self.assertEqual(self.get_string_for_nodes(test), result)  # add assertion here

    def test_move_nodes(self):
        root = SimpleTreeNode('root', None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode('node1', None)
        node2 = SimpleTreeNode('node2', None)
        node3 = SimpleTreeNode('node3', None)
        node4 = SimpleTreeNode('node4', None)
        tree.AddChild(root, node1)
        tree.AddChild(root, node2)
        tree.AddChild(node2, node3)
        tree.AddChild(node3, node4)
        tree.MoveNode(node4, node2)
        result = '[root,None][node1,root][node2,root][node3,node2][node4,node2]'
        self.assertEqual(self.get_string_for_tree(tree), result)  # add assertion here

    def test_count_nodes(self):
        root = SimpleTreeNode('root', None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode('node1', None)
        tree.AddChild(root, node1)
        node2 = SimpleTreeNode('node2', None)
        node3 = SimpleTreeNode('node3', None)
        node4 = SimpleTreeNode('node4', None)
        self.assertEqual(tree.Count(), 2)  # add assertion here

    def test_count_leaves(self):
        root = SimpleTreeNode('root', None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode('node1', None)
        node2 = SimpleTreeNode('node2', None)
        node3 = SimpleTreeNode('node3', None)
        node4 = SimpleTreeNode('node4', None)
        tree.AddChild(root, node1)
        tree.AddChild(root, node2)
        tree.AddChild(node2, node3)
        tree.AddChild(node3, node4)
        self.assertEqual(tree.LeafCount(), 2)  # add assertion here

    def test_count_leaves(self):
        root = SimpleTreeNode('root', None)
        tree = SimpleTree(root)
        node1 = SimpleTreeNode('node1', None)
        node2 = SimpleTreeNode('node2', None)
        node3 = SimpleTreeNode('node3', None)
        node4 = SimpleTreeNode('node4', None)
        tree.AddChild(root, node1)
        tree.AddChild(root, node2)
        tree.AddChild(node2, node3)
        tree.AddChild(node3, node4)
        tree.set_levels()
        result = '[root,None,1][node1,root,2][node2,root,2][node3,node2,3][node4,node3,4]'
        self.assertEqual(self.get_string_for_tree_with_levels(tree), result)  # add assertion here


    def get_string_for_tree(self, tree):
        string = ''
        all_nodes = tree.GetAllNodes()
        for node in all_nodes:
            parent_val = 'None' if node.Parent is None else str(node.Parent.NodeValue)
            string += '[' + str(node.NodeValue) + ',' + parent_val + ']'
        return string

    def get_string_for_tree_with_levels(self, tree):
        string = ''
        all_nodes = tree.GetAllNodes()
        for node in all_nodes:
            parent_val = 'None' if node.Parent is None else str(node.Parent.NodeValue)
            string += '[' + str(node.NodeValue) + ',' + parent_val + ',' + str(node.level) +']'
        return string

    def get_string_for_nodes(self, nodes):
        string = ''
        for node in nodes:
            parent_val = 'None' if node.Parent is None else str(node.Parent.NodeValue)
            string += '[' + str(node.NodeValue) + ',' + parent_val + ']'
        return string



if __name__ == '__main__':
    unittest.main()
