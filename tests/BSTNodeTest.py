import unittest

from BSTNode import BSTNode, BST, BSTFind


class MyTestCase(unittest.TestCase):

    def test_find_100(self):
        root = BSTNode(8, 0, None)
        tree = BST(root)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)

        expected_bst = '[8,0,None,4,12][4,4,8,2,6][2,2,4,1,3][1,1,2,None,None]' \
                       '[3,3,2,None,None][6,6,4,5,7][5,5,6,None,None][7,7,6,None,None]' \
                       '[12,12,8,10,14][10,10,12,9,11][9,9,10,None,None][11,11,10,None,None]' \
                       '[14,14,12,13,15][13,13,14,None,None][15,15,14,None,None]'

        self.assertEqual(expected_bst, self.get_string_for_tree(tree))

        expected_bst_find = '15,False,False'
        bst_find = tree.FindNodeByKey(100)
        self.assertEqual(expected_bst_find, self.get_string_for_bst_find(bst_find))

        self.assertEqual(False, bst_find.NodeHasKey)
        self.assertEqual(False, bst_find.ToLeft)
        self.assertEqual(tree.FindNodeByKey(15).Node, bst_find.Node)
        self.assertEqual(15, bst_find.Node.NodeKey)
        self.assertEqual(tree.FindNodeByKey(14).Node, bst_find.Node.Parent)
        self.assertEqual(14, bst_find.Node.Parent.NodeKey)

        expected_bst_find = '1,False,True'
        bst_find = tree.FindNodeByKey(0)
        self.assertEqual(expected_bst_find, self.get_string_for_bst_find(bst_find))

        self.assertEqual(False, bst_find.NodeHasKey)
        self.assertEqual(True, bst_find.ToLeft)
        self.assertEqual(tree.FindNodeByKey(1).Node, bst_find.Node)
        self.assertEqual(1, bst_find.Node.NodeKey)
        self.assertEqual(tree.FindNodeByKey(2).Node, bst_find.Node.Parent)
        self.assertEqual(2, bst_find.Node.Parent.NodeKey)

    def bst_find_to_str_full(self, bst_find):
        node = bst_find.Node
        if node:
            node_str = '[' + str(node.NodeKey) + ',' + str(node.Parent.NodeKey) + ']'
        else:
            node_str = 'None'
        return node_str + ',' + str(bst_find.NodeHasKey) + ',' + str(bst_find.ToLeft)



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
        tree = BST(None)
        bst_find = tree.FindNodeByKey(0)
        self.assertEqual(None, bst_find)  # add assertion here

        root = BSTNode(5, 5, None)
        node2 = BSTNode(3, 3, root)
        node3 = BSTNode(7, 7, root)
        root.LeftChild = node2
        root.RightChild = node3
        tree = BST(root)

        bst_find = tree.FindNodeByKey(5)
        self.assertEqual('5,True,False', self.bst_find_to_str(bst_find))

        bst_find = tree.FindNodeByKey(1)
        self.assertEqual('3,False,True', self.bst_find_to_str(bst_find))

        bst_find = tree.FindNodeByKey(6)
        self.assertEqual('7,False,True', self.bst_find_to_str(bst_find))

        bst_find = tree.FindNodeByKey(10)
        self.assertEqual('7,False,False', self.bst_find_to_str(bst_find))

    @staticmethod
    def bst_find_to_str(bst_find):
        node = bst_find.Node.NodeKey if bst_find.Node else 'None'
        return str(node) + ',' + str(bst_find.NodeHasKey) + ',' + str(bst_find.ToLeft)

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
        expected_node = tree.FindNodeByKey(10).Node
        actual_node = tree.FinMinMax(root, True)
        self.assertEqual(expected_node, actual_node)  # add assertion here

    def test_find_min_root(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(10, 10)
        expected_bst_find = BSTFind()
        expected_node = tree.FindNodeByKey(1).Node
        actual_node = tree.FinMinMax(root, False)
        self.assertEqual(expected_node, actual_node)  # add assertion here

    def test_find_max_not_root(self):
        root = BSTNode(5, 5, None)
        tree = BST(root)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(10, 10)
        start_node = tree.FindNodeByKey(7).Node
        expected_node = tree.FindNodeByKey(10).Node
        actual_node = tree.FinMinMax(start_node, True)
        self.assertEqual(expected_node, actual_node)  # add assertion here

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

    @staticmethod
    def get_string_for_tree(tree):
        string = ''
        all_nodes = tree.get_all_nodes()
        for node in all_nodes:
            parent_val = str(node.Parent.NodeKey) if node.Parent else 'None'
            left_val = str(node.LeftChild.NodeKey) if node.LeftChild else 'None'
            right_val = str(node.RightChild.NodeKey) if node.RightChild else 'None'
            string += '[' + str(node.NodeKey) + ',' + str(node.NodeValue) + ',' + parent_val + ',' +\
                      left_val + ',' + right_val + ']'
        return string

    @staticmethod
    def get_string_for_bst_find(bst_find):
        node_value = str(bst_find.Node.NodeKey) if bst_find.Node else 'None'
        return node_value + ',' + str(bst_find.NodeHasKey) + ',' + str(bst_find.ToLeft)

    def test_wide(self):
        root = BSTNode(8, 0, None)
        tree = BST(root)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)

        all_nodes = tree.WideAllNodes()

        expected_bst = '[8,0,None,4,12]' \
                       '[4,4,8,2,6]' \
                       '[12,12,8,10,14]' \
                       '[2,2,4,1,3]' \
                       '[6,6,4,5,7]' \
                       '[10,10,12,9,11]' \
                       '[14,14,12,13,15]' \
                       '[1,1,2,None,None]' \
                       '[3,3,2,None,None]' \
                       '[5,5,6,None,None]' \
                       '[7,7,6,None,None]' \
                       '[9,9,10,None,None]' \
                       '[11,11,10,None,None]' \
                       '[13,13,14,None,None]' \
                       '[15,15,14,None,None]'

        self.assertEqual(expected_bst, self.get_string_for_nodes(all_nodes))

    def test_deep_in_order(self):
        root = BSTNode(8, 0, None)
        tree = BST(root)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)

        all_nodes = tree.DeepAllNodes(0)

        expected_bst = '[1,1,2,None,None]' \
                       '[2,2,4,1,3]' \
                       '[3,3,2,None,None]' \
                       '[4,4,8,2,6]' \
                       '[5,5,6,None,None]' \
                       '[6,6,4,5,7]' \
                       '[7,7,6,None,None]' \
                       '[8,0,None,4,12]' \
                       '[9,9,10,None,None]' \
                       '[10,10,12,9,11]' \
                       '[11,11,10,None,None]' \
                       '[12,12,8,10,14]' \
                       '[13,13,14,None,None]' \
                       '[14,14,12,13,15]' \
                       '[15,15,14,None,None]'

        self.assertEqual(expected_bst, self.get_string_for_nodes(all_nodes))

    def test_deep_post_order(self):
        root = BSTNode(8, 0, None)
        tree = BST(root)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)

        all_nodes = tree.DeepAllNodes(1)

        expected_bst = '[1,1,2,None,None]' \
                       '[3,3,2,None,None]' \
                       '[2,2,4,1,3]' \
                       '[5,5,6,None,None]' \
                       '[7,7,6,None,None]' \
                       '[6,6,4,5,7]' \
                       '[4,4,8,2,6]' \
                       '[9,9,10,None,None]' \
                       '[11,11,10,None,None]' \
                       '[10,10,12,9,11]' \
                       '[13,13,14,None,None]' \
                       '[15,15,14,None,None]' \
                       '[14,14,12,13,15]' \
                       '[12,12,8,10,14]' \
                       '[8,0,None,4,12]' \


        self.assertEqual(expected_bst, self.get_string_for_nodes(all_nodes))

    def test_deep_pre_order(self):
        root = BSTNode(8, 0, None)
        tree = BST(root)
        tree.AddKeyValue(4, 4)
        tree.AddKeyValue(12, 12)
        tree.AddKeyValue(2, 2)
        tree.AddKeyValue(6, 6)
        tree.AddKeyValue(10, 10)
        tree.AddKeyValue(14, 14)
        tree.AddKeyValue(1, 1)
        tree.AddKeyValue(3, 3)
        tree.AddKeyValue(5, 5)
        tree.AddKeyValue(7, 7)
        tree.AddKeyValue(9, 9)
        tree.AddKeyValue(11, 11)
        tree.AddKeyValue(13, 13)
        tree.AddKeyValue(15, 15)

        all_nodes = tree.DeepAllNodes(2)

        expected_bst = '[8,0,None,4,12]' \
                       '[4,4,8,2,6]' \
                       '[12,12,8,10,14]' \
                       '[2,2,4,1,3]' \
                       '[6,6,4,5,7]' \
                       '[10,10,12,9,11]' \
                       '[14,14,12,13,15]' \
                       '[1,1,2,None,None]' \
                       '[3,3,2,None,None]' \
                       '[5,5,6,None,None]' \
                       '[7,7,6,None,None]' \
                       '[9,9,10,None,None]' \
                       '[11,11,10,None,None]' \
                       '[13,13,14,None,None]' \
                       '[15,15,14,None,None]'


        self.assertEqual(expected_bst, self.get_string_for_nodes(all_nodes))


    @staticmethod
    def get_string_for_nodes(all_nodes):
        string = ''
        for node in all_nodes:
            parent_val = str(node.Parent.NodeKey) if node.Parent else 'None'
            left_val = str(node.LeftChild.NodeKey) if node.LeftChild else 'None'
            right_val = str(node.RightChild.NodeKey) if node.RightChild else 'None'
            string += '[' + str(node.NodeKey) + ',' + str(node.NodeValue) + ',' + parent_val + ',' + \
                      left_val + ',' + right_val + ']'
        return string


if __name__ == '__main__':
    unittest.main()
