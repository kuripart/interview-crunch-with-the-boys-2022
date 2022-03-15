# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the 'true'
# length of the string.


# O(n^2) time and space complexity for worst case based on this discussion https://stackoverflow.com/questions/35583983/what-is-the-big-o-notation-for-the-str-replace-function-in-python
def url_ify(input_str):
    input_str = input_str.strip().replace(' ', '%20')
    return input_str


import unittest

class TestURLify(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(url_ify('Mr John Smith'), 'Mr%20John%20Smith')
        self.assertEqual(url_ify('Aa bB cC'), 'Aa%20bB%20cC')
    
    def test_trailing(self):
        self.assertEqual(url_ify('    Mr John Smith   '), 'Mr%20John%20Smith')
        self.assertEqual(url_ify('     Aa bB cC     '), 'Aa%20bB%20cC')


if __name__ == '__main__':
    unittest.main()
