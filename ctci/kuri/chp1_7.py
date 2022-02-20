def solve(matrix):
    # Eg 2D Array
    # w, h = 8, 5
    # Matrix = [[0 for x in range(w)] for y in range(h)] 
    # return Matrix

    zeroes = []

   # O(rows x cols)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                zeroes.append((row, col),)
    
    if zeroes == []:
        return matrix

    # O(num of zeroes x rows x cols)
    for zero_coord in zeroes:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row == zero_coord[0]:
                    matrix[row][col] = 0
                if col == zero_coord[1]:
                    matrix[row][col] = 0

    return matrix

    

# Time: (rows^2 x cols^2) ?
# Space: O(rows x cols) # number of zeroes - worst case

import unittest

class TestSum(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve([[1,0,1],[2,2,2],[0,3,3]]), [[0,0,0],[0,0,2],[0,0,0]])
        self.assertEqual(solve([[1,0,0],[2,2,2],[3,3,3]]), [[0,0,0],[2,0,0],[3,0,0]])

if __name__ == '__main__':
    unittest.main()


###################
## Before
# 1 0 1
# 2 2 2
# 0 3 3

## After
# 0 2 1
# 3 2 0
# 3 2 1
###################