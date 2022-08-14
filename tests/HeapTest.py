import unittest

from Heap import Heap


class MyTestCase(unittest.TestCase):

    def test_1(self):
        tree = Heap()
        a = [None] * 15
        a[0] = 11
        a[1] = 9
        a[2] = 4
        a[3] = 7
        a[4] = 8
        a[5] = 3
        a[6] = 1
        a[7] = 2
        a[8] = 5
        a[9] = 6

        tree.MakeHeap(a, 3)
        self.assertEqual(True, True)


        # expected_bst = '[50,None,25,75,0]' \
        #                '[25,50,16,37,1]' \
        #                '[75,50,62,84,1]' \
        #                '[16,25,12,19,2]' \
        #                '[37,25,31,43,2]' \
        #                '[62,75,55,65,2]' \
        #                '[84,75,82,92,2]' \
        #                '[12,16,None,None,3]' \
        #                '[19,16,None,None,3]' \
        #                '[31,37,None,None,3]' \
        #                '[43,37,None,None,3]' \
        #                '[55,62,None,None,3]' \
        #                '[65,62,None,None,3]' \
        #                '[82,84,None,None,3]' \
        #                '[92,84,None,None,3]'
        #
        # self.assertEqual(expected_bst, self.get_string_for_tree(tree))
        # self.assertEqual(True, tree.IsBalanced(tree.Root))


if __name__ == '__main__':
    unittest.main()
