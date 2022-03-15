# String Rotation: Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to i5Sub5tring (e.g., "waterbottle" is a rotation of" erbottlewat").

# O(n) time and space
def is_string_rotation(s1, s2):
    # If string s1 is splity between x and y to rotate, s2 should be yx
    # If there is a string xyxy, yx will always be a substring of it
    # Extrapolating this, if s1s1 has s2 as a substring, we can identify that s2 is a rotation of s1
    return s2 in s1+s1


import unittest

class TestStringRotation(unittest.TestCase):
    def test_is_string_rotated(self):
        self.assertEqual(is_string_rotation('', ''), True)
        self.assertEqual(is_string_rotation('waterbottle', 'erbottlewat'), True)
        self.assertEqual(is_string_rotation('waterbottle', 'rebottlewat'), False)
        self.assertEqual(is_string_rotation('bottleBottle', 'Bottlebottle'), True)
        self.assertEqual(is_string_rotation('a', 'a'), True)


if __name__ == '__main__':
    unittest.main()
