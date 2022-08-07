import unittest

from GenerateBBSTArray import GenerateBBSTArray


class MyTestCase(unittest.TestCase):

    def test_generate(self):
        # depth = 3
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
        # [12, 16, 19, 25, 31, 37, 43, 50, 55, 62, 65, 75, 84, 90, 92]
        # 50, 25, 75, 16, 37, 62, 84, 12, 19, 31, 43, 55, 65, 82, 92
        new_array = GenerateBBSTArray(a)
        self.assertEqual('[50, 25, 75, 16, 37, 62, 84, 12, 19, 31, 43, 55, 65, 82, 92]', str(new_array))  # add assertion here


if __name__ == '__main__':
    unittest.main()
