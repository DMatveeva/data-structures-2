import unittest

from aBST import aBST


class MyTestCase(unittest.TestCase):

    # depth = 0
    def test_FindKeyIndex_1(self):
        tree = aBST(0)
        element = tree.FindKeyIndex(8)
        self.assertEqual(0, element)

    def test_FindKeyIndex_2(self):
        tree = aBST(0)
        tree.Tree[0] = 8
        element = tree.FindKeyIndex(8)
        self.assertEqual(0, element)

    def test_FindKeyIndex_3(self):
        tree = aBST(3)
        tree.Tree[0] = 50
        tree.Tree[1] = 25
        tree.Tree[2] = 75
        tree.Tree[3] = None
        tree.Tree[4] = 37
        tree.Tree[5] = 62
        tree.Tree[6] = 84
        tree.Tree[7] = None
        tree.Tree[8] = None
        tree.Tree[9] = 31
        tree.Tree[10] = 43
        tree.Tree[11] = 55
        tree.Tree[12] = None
        tree.Tree[13] = None
        tree.Tree[14] = 92
        self.assertEqual(0, tree.FindKeyIndex(50))
        self.assertEqual(1, tree.FindKeyIndex(25))
        self.assertEqual(2, tree.FindKeyIndex(75))
        self.assertEqual(4, tree.FindKeyIndex(37))
        self.assertEqual(5, tree.FindKeyIndex(62))
        self.assertEqual(6, tree.FindKeyIndex(84))
        self.assertEqual(9, tree.FindKeyIndex(31))
        self.assertEqual(10, tree.FindKeyIndex(43))
        self.assertEqual(11, tree.FindKeyIndex(55))
        self.assertEqual(14, tree.FindKeyIndex(92))

        self.assertEqual(-3, tree.FindKeyIndex(16))
        self.assertEqual(-12, tree.FindKeyIndex(67))
        self.assertEqual(-13, tree.FindKeyIndex(79))
        self.assertEqual(None, tree.FindKeyIndex(100))

    def test_AddKey(self):
        tree = aBST(0)

        self.assertEqual(0, tree.AddKey(50))
        self.assertEqual(50, tree.Tree[0])
        self.assertEqual(0, tree.AddKey(50))

    def test_AddKey(self):
        tree = aBST(3)

        self.assertEqual(0, tree.AddKey(50))
        self.assertEqual(50, tree.Tree[0])

        self.assertEqual(1, tree.AddKey(25))
        self.assertEqual(25, tree.Tree[1])

        self.assertEqual(2, tree.AddKey(75))
        self.assertEqual(75, tree.Tree[2])

        self.assertEqual(4, tree.AddKey(37))
        self.assertEqual(37, tree.Tree[4])

        self.assertEqual(5, tree.AddKey(62))
        self.assertEqual(62, tree.Tree[5])

        self.assertEqual(6, tree.AddKey(84))
        self.assertEqual(84, tree.Tree[6])

        self.assertEqual(9, tree.AddKey(31))
        self.assertEqual(31, tree.Tree[9])

        self.assertEqual(10, tree.AddKey(43))
        self.assertEqual(43, tree.Tree[10])

        self.assertEqual(11, tree.AddKey(55))
        self.assertEqual(55, tree.Tree[11])

        self.assertEqual(14, tree.AddKey(92))
        self.assertEqual(92, tree.Tree[14])

        self.assertEqual(3, tree.AddKey(16))
        self.assertEqual(16, tree.Tree[3])

        self.assertEqual(12, tree.AddKey(67))
        self.assertEqual(67, tree.Tree[12])

        self.assertEqual(13, tree.AddKey(79))
        self.assertEqual(79, tree.Tree[13])

        self.assertEqual(-1, tree.AddKey(100))



if __name__ == '__main__':
    unittest.main()
