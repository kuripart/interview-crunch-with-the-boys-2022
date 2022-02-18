# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


# O(n) space and time
def string_compression(input_str):
    input_str_len = len(input_str)
    if input_str_len <= 1:
        return input_str

    prev_char = input_str[0]
    char_count = 1
    ret_list = list()
    for c in input_str[1:input_str_len]:
        if prev_char != c:
            append_char_count(prev_char, char_count, ret_list)
            prev_char = c
            char_count = 1
        else:
            char_count += 1

    append_char_count(prev_char, char_count, ret_list)
    ret_str = ''.join(ret_list)

    return input_str if len(ret_str) >= input_str_len else ret_str

def append_char_count(prev_char, char_count, return_str):
    return_str.append(prev_char + str(char_count))
    return return_str


import unittest

class TestStringCompression(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(string_compression('aabcccccaaa'), 'a2b1c5a3')

    def test_compressed_larger(self):
        self.assertEqual(string_compression('abcdef'), 'abcdef')

    def test_caps(self):
        self.assertEqual(string_compression('aaaaaAAAA'), 'a5A4')
    
    def test_empty(self):
        self.assertEqual(string_compression(''), '')
    
    def test_single_char(self):
        self.assertEqual(string_compression('a'), 'a')


if __name__ == '__main__':
    unittest.main()