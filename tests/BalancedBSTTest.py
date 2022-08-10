import unittest

from BalancedBST import BalancedBST


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_FindKeyIndex_1(self):
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
        print(tree.IsBalanced(tree.Root))



if __name__ == '__main__':
    unittest.main()
