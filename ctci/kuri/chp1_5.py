def solve(str1, str2):

    if str1 == str2:
        return True

    str2_len = len(str2)
    str1_len = len(str1)

    # base cases
    if str2_len == str1_len:
        pass
    else:
        str2_len = len(str2)
        str1_len = len(str1)
        if abs(str2_len - str1_len) >= 2:
            return False

    cnt1 = 0
    cnt2 = 0

    # find the shortest and longest string
    shortest = str1 if str1_len <= str2_len else str2
    longest = str1 if str1_len > str2_len else str2
    
    diff = 0
    while cnt1 < len(longest) and cnt2 < len(shortest):
        if str1_len == str2_len:
            if longest[cnt1] != shortest[cnt2]:
                diff += 1
            cnt2 += 1
            cnt1 += 1
        else:
            if longest[cnt1] == shortest[cnt2]:
                cnt2 += 1
            else:
                diff += 1
            cnt1 += 1

    return True if diff in (0,1) else False

# Time: O(n)
# Space: O(1)

import unittest

class TestSum(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("pale", "ple"), True)
        self.assertEqual(solve("pales", "pale"), True)
        self.assertEqual(solve("pale", "bale"), True)
        self.assertEqual(solve("pale", "bake"), False)
        self.assertEqual(solve("pale", "pale"), True)
        self.assertEqual(solve("pale", "pl"), False)

if __name__ == '__main__':
    unittest.main()