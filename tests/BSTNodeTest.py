import unittest

from BSTNode import BSTNode, BST, BSTFind


class MyTestCase(unittest.TestCase):

    def test_add_to_left_2(self):
        root = BSTNode(5, 5, None)
        node2 = BSTNode(3, 3, root)
        node3 = BSTNode(7, 7, root)
        root.LeftChild = node2
        root.RightChild = node3
        tree = BST(root)
        is_added = tree.AddKeyValue(1, 1)
        new_tree = '[5,5,None,3,7][3,3,5,1,None][1,1,3,None,None][7,7,5,None,None]'
        self.assertEqual(is_added, True)  # add assertion here
        self.assertEqual(self.get_string_for_tree(tree), new_tree)  # add assertion here

    def test_add_3(self):
        tree = BST(None)
        tree.AddKeyValue(1, 1)
        expected_tree = '[1,1,None,None,None]'
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))
        tree.AddKeyValue(4, 4)
        expected_tree = '[1,1,None,None,4][4,4,1,None,None]'
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))
        tree.AddKeyValue(-1, -1)
        expected_tree = '[1,1,None,-1,4][-1,-1,1,None,None][4,4,1,None,None]'
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))

        tree.AddKeyValue(10, 10)
        expected_tree = '[1,1,None,-1,4][-1,-1,1,None,None][4,4,1,None,10][10,10,4,None,None]'
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))

        tree.AddKeyValue(100, 3)
        expected_tree = '[1,1,None,-1,4][-1,-1,1,None,None][4,4,1,None,10][10,10,4,None,100][100,3,10,None,None]'
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))

        tree.AddKeyValue(100, 8)
        expected_tree = '[1,1,None,-1,4][-1,-1,1,None,None][4,4,1,None,10][10,10,4,None,100][100,3,10,None,None]'
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))

        tree.AddKeyValue(7, 8)
        expected_tree = '[1,1,None,-1,4][-1,-1,1,None,None][4,4,1,None,10][10,10,4,7,100][7,8,10,None,None][100,3,10,None,None]'
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))

    def test_delete_by_key_root(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(10, 10)
        is_deleted = tree.DeleteNodeByKey(5)
        expected_tree = '[7,7,None,6,9][6,6,7,None,None][9,9,7,None,10][10,10,9,None,None]'
        self.assertEqual(True, is_deleted)
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))

    def test_delete_by_key_with_2_children(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(10, 10)
        is_deleted = tree.DeleteNodeByKey(7)
        expected_tree = '[5,5,None,None,9][9,9,5,6,10][6,6,9,None,None][10,10,9,None,None]'
        self.assertEqual(True, is_deleted)
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))

    def test_find_equal(self):
        root = BSTNode(5, 5, None)
        node2 = BSTNode(3, 3, root)
        node3 = BSTNode(7, 7, root)
        root.LeftChild = node2
        root.RightChild = node3
        tree = BST(root)
        bst_find = tree.FindNodeByKey(3)
        test_bst_find = BSTFind()
        test_bst_find.Node = node2
        test_bst_find.NodeHasKey = True
        self.assertEqual(self.bst_find_to_str(bst_find), self.bst_find_to_str(test_bst_find))


    def bst_find_to_str(self, bst_find):
        node = bst_find.Node.NodeKey if bst_find.Node else 'None'
        return str(node) + ',' + str(bst_find.NodeHasKey) + ',' + str(bst_find.ToLeft)

    def test_find_left(self):
        root = BSTNode(5, 5, None)
        node2 = BSTNode(3, 3, root)
        node3 = BSTNode(7, 7, root)
        root.LeftChild = node2
        root.RightChild = node3
        tree = BST(root)
        bst_find = tree.FindNodeByKey(1)
        test_bst_find = BSTFind()
        test_bst_find.Node = node2
        test_bst_find.NodeHasKey = False
        test_bst_find.ToLeft = True
        self.assertEqual(self.bst_find_to_str(bst_find), self.bst_find_to_str(test_bst_find))  # add assertion here

    def test_find(self):
        root = BSTNode(5, 5, None)
        node2 = BSTNode(3, 3, root)
        node3 = BSTNode(7, 7, root)
        root.LeftChild = node2
        root.RightChild = node3
        tree = BST(root)
        bst_find = tree.FindNodeByKey(1)
        self.assertEqual('3,False,True', self.bst_find_to_str(bst_find))  # add assertion here

    def test_find(self):
        tree = BST(None)
        bst_find = tree.FindNodeByKey(1)
        self.assertEqual('None,False,False', self.bst_find_to_str(bst_find))  # add assertion here

    def test_find_right(self):
        root = BSTNode(5, 5, None)
        node2 = BSTNode(3, 3, root)
        node3 = BSTNode(7, 7, root)
        root.LeftChild = node2
        root.RightChild = node3
        tree = BST(root)
        bst_find = tree.FindNodeByKey(9)
        test_bst_find = BSTFind()
        test_bst_find.Node = node3
        test_bst_find.NodeHasKey = False
        test_bst_find.ToLeft = False
        self.assertEqual(self.bst_find_to_str(bst_find), self.bst_find_to_str(test_bst_find))  # add assertion here

    def test_add_existing(self):
        root = BSTNode(5, 5, None)
        node2 = BSTNode(3, 3, root)
        node3 = BSTNode(7, 7, root)
        root.LeftChild = node2
        root.RightChild = node3
        tree = BST(root)
        is_added = tree.AddKeyValue(3, 10)
        self.assertEqual(is_added, False)  # add assertion here

    def test_add_to_left(self):
        root = BSTNode(5, 5, None)
        node2 = BSTNode(3, 3, root)
        node3 = BSTNode(7, 7, root)
        root.LeftChild = node2
        root.RightChild = node3
        tree = BST(root)
        is_added = tree.AddKeyValue(1, 10)
        new_tree = '[5,5,None,3,7][3,3,5,1,None][1,10,3,None,None][7,7,5,None,None]'
        self.assertEqual(is_added, True)  # add assertion here
        self.assertEqual(self.get_string_for_tree(tree), new_tree)  # add assertion here

    def test_add_to_right(self):
        root = BSTNode(5, 5, None)
        node2 = BSTNode(3, 3, root)
        node3 = BSTNode(7, 7, root)
        root.LeftChild = node2
        root.RightChild = node3
        tree = BST(root)
        is_added = tree.AddKeyValue(9, 10)
        new_tree = '[5,5,None,3,7][3,3,5,None,None][7,7,5,None,9][9,10,7,None,None]'
        self.assertEqual(is_added, True)  # add assertion here
        self.assertEqual(self.get_string_for_tree(tree), new_tree)  # add assertion here

    def test_find_max_root(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(10, 10)
        expected_bst_find = BSTFind()
        correct_node = tree.FindNodeByKey(10).Node
        expected_bst_find.Node = correct_node
        expected_bst_find.NodeHasKey = True
        bst_find_to_check = tree.FinMinMax(root, True)
        self.assertEqual(self.get_string_for_bst_find(expected_bst_find), self.get_string_for_bst_find(bst_find_to_check))  # add assertion here

    def test_find_min_root(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(10, 10)
        expected_bst_find = BSTFind()
        correct_node = tree.FindNodeByKey(1).Node
        expected_bst_find.Node = correct_node
        expected_bst_find.NodeHasKey = True
        bst_find_to_check = tree.FinMinMax(root, False)
        self.assertEqual(self.get_string_for_bst_find(expected_bst_find), self.get_string_for_bst_find(bst_find_to_check))  # add assertion here

    def test_find_max_not_root(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(10, 10)
        start_node = tree.FindNodeByKey(7).Node
        expected_bst_find = BSTFind()
        correct_node = tree.FindNodeByKey(10).Node
        expected_bst_find.Node = correct_node
        expected_bst_find.NodeHasKey = True
        bst_find_to_check = tree.FinMinMax(start_node, True)
        self.assertEqual(self.get_string_for_bst_find(expected_bst_find), self.get_string_for_bst_find(bst_find_to_check))  # add assertion here

    def test_find_min_not_root(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(10, 10)
        start_node = tree.FindNodeByKey(3).Node
        expected_bst_find = BSTFind()
        correct_node = tree.FindNodeByKey(1).Node
        expected_bst_find.Node = correct_node
        expected_bst_find.NodeHasKey = True
        bst_find_to_check = tree.FinMinMax(start_node, False)
        self.assertEqual(self.get_string_for_bst_find(expected_bst_find), self.get_string_for_bst_find(bst_find_to_check))  # add assertion here

    def test_delete_by_key_with_no_child(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(10, 10)
        is_deleted = tree.DeleteNodeByKey(0)
        self.assertEqual(False, is_deleted)

    def test_delete_by_key_with_onde_child(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(7, 7)
        is_deleted = tree.DeleteNodeByKey(3)
        expected_tree = '[5,5,None,None,7][7,7,5,None,None]'
        self.assertEqual(True, is_deleted)
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))


    def test_delete_by_key_with_2_children_no_update(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(8, 8)
        is_deleted = tree.DeleteNodeByKey(7)
        expected_tree = '[5,5,None,None,8][8,8,5,6,9][6,6,8,None,None][9,9,8,None,None]'
        self.assertEqual(True, is_deleted)
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))

    def test_find_min_not_root(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(1, 1)
        is_deleted = tree.DeleteNodeByKey(3)
        self.assertEqual(True, is_deleted)
        expected_tree = '[5,5,None,1,None][1,1,5,None,None]'
        self.assertEqual(expected_tree, self.get_string_for_tree(tree))



    def get_string_for_tree(self, tree):
        string = ''
        all_nodes = tree.GetAllNodes()
        for node in all_nodes:
            parent_val = str(node.Parent.NodeKey) if node.Parent else 'None'
            left_val = str(node.LeftChild.NodeKey) if node.LeftChild else 'None'
            right_val = str(node.RightChild.NodeKey) if node.RightChild else 'None'
            string += '[' + str(node.NodeKey) + ',' + str(node.NodeValue) + ',' + parent_val + ',' +\
                      left_val + ',' + right_val + ']'
        return string

    def get_string_for_bst_find(self, bst_find):
        node_value = str(bst_find.Node.NodeKey) if bst_find.Node else 'None'
        return node_value + ',' + str(bst_find.NodeHasKey) + ',' + str(bst_find.ToLeft)


if __name__ == '__main__':
    unittest.main()
