import unittest

from BalancedBST import BalancedBST


class MyTestCase(unittest.TestCase):


    def test_1(self):
        tree = BalancedBST()
        a = [None] * 15
        a[0] = 50
        a[1] = 92
        a[2] = 84
        a[3] = 62
        a[4] = 75
        a[5] = 43
        a[6] = 31
        a[7] = 37
        a[8] = 55
        a[9] = 25
        a[10] = 16
        a[11] = 19
        a[12] = 12
        a[13] = 65
        a[14] = 82
        tree.GenerateTree(a)

        expected_bst = '[50,None,25,75,0]' \
                       '[25,50,16,37,1]' \
                       '[75,50,62,84,1]' \
                       '[16,25,12,19,2]' \
                       '[37,25,31,43,2]' \
                       '[62,75,55,65,2]' \
                       '[84,75,82,92,2]' \
                       '[12,16,None,None,3]' \
                       '[19,16,None,None,3]' \
                       '[31,37,None,None,3]' \
                       '[43,37,None,None,3]' \
                       '[55,62,None,None,3]' \
                       '[65,62,None,None,3]' \
                       '[82,84,None,None,3]' \
                       '[92,84,None,None,3]'

        self.assertEqual(expected_bst, self.get_string_for_tree(tree))
        self.assertEqual(True, tree.IsBalanced(tree.Root))

    def test_1(self):
        tree = BalancedBST()
        a = [None] * 5
        a[0] = 50
        a[1] = 92
        a[2] = 84
        a[3] = 75
        a[4] = 25

        tree.GenerateTree(a)

        expected_bst = '[50,None,25,75,0]' \
                       '[25,50,None,None,1]' \
                       '[75,50,None,84,1]' \
                       '[84,75,None,92,2]' \
                       '[92,84,None,None,3]'

        self.assertEqual(expected_bst, self.get_string_for_tree(tree))
        self.assertEqual(False, tree.IsBalanced(tree.Root))



    @staticmethod
    def get_string_for_tree(tree):
        all_nodes = tree.WideAllNodes()
        string = ''
        for node in all_nodes:
            parent_val = str(node.Parent.NodeKey) if node.Parent else 'None'
            left_val = str(node.LeftChild.NodeKey) if node.LeftChild else 'None'
            right_val = str(node.RightChild.NodeKey) if node.RightChild else 'None'
            string += '[' + str(node.NodeKey) + ',' + parent_val + ',' + \
                      left_val + ',' + right_val + ',' + str(node.Level) + ']'
        return string

if __name__ == '__main__':
    unittest.main()
