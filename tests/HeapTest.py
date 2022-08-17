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
        expected_bst = '11,9,4,7,8,3,1,2,5,6,n,n,n,n,n,'
        self.assertEqual(expected_bst, self.get_string_for_tree(tree))

    def get_string_for_tree(self, heap):
        string = ''
        for element in heap.HeapArray:
            s = str(element) if element else 'n'
            string += s + ','
        return string

    def test_2(self):
        tree = Heap()
        a = [None] * 15
        tree.MakeHeap(a, 3)
        expected_bst = 'n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected_bst, self.get_string_for_tree(tree))

    def test_3(self):
        tree = Heap()
        a = [None] * 15
        tree.MakeHeap(a, 3)
        actual = tree.GetMax()
        self.assertEqual(-1, actual)

    def test_4(self):
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
        actual = tree.GetMax()
        self.assertEqual(11, actual)
        expected = '9,8,4,7,6,3,1,2,5,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(9, actual)
        expected = '8,7,4,5,6,3,1,2,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(8, actual)
        expected = '7,6,4,5,2,3,1,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(7, actual)
        expected = '6,5,4,1,2,3,n,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(6, actual)
        expected = '5,3,4,1,2,n,n,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(5, actual)
        expected = '4,3,2,1,n,n,n,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(4, actual)
        expected = '3,1,2,n,n,n,n,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(3, actual)
        expected = '2,1,n,n,n,n,n,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(2, actual)
        expected = '1,n,n,n,n,n,n,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(1, actual)
        expected = 'n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

        actual = tree.GetMax()
        self.assertEqual(-1, actual)
        expected = 'n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))

    def test_5(self):
        tree = Heap()
        a = [None] * 7
        a[0] = 11
        a[1] = 9
        a[2] = 4
        a[3] = 7
        a[4] = 8
        a[5] = 3
        a[6] = 1

        tree.MakeHeap(a, 2)
        actual = tree.GetMax()
        self.assertEqual(11, actual)
        expected = '9,8,4,7,1,3,n,'
        self.assertEqual(expected, self.get_string_for_tree(tree))



    def get_string_for_tree(self, heap):
        string = ''
        for element in heap.HeapArray:
            s = str(element) if element else 'n'
            string += s + ','
        return string



if __name__ == '__main__':
    unittest.main()
