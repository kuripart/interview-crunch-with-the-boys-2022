def solve(str1, str2):
    return sorted(str1) == sorted(str2)

# Time: O(nlogn)
# Space: O(n) : Assuming sorting strings need extra space

import unittest

class TestSum(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("hello", "elloh"), True)
        self.assertEqual(solve("hello", "olleh"), True)
        self.assertEqual(solve("hello", "hello"), True)
        self.assertEqual(solve("okay", "elloh"), False)
        self.assertEqual(solve("bye", "elloh"), False)
        self.assertEqual(solve("hi", "ih"), True)
        self.assertEqual(solve("", ""), True)
        self.assertEqual(solve("hello", ""), False)
        self.assertEqual(solve("", "elloh"), False)


if __name__ == '__main__':
    unittest.main()