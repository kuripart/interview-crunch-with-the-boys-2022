from dataclasses import dataclass


class EmptyException(Exception):
    pass


@dataclass
class Stack:
    data: list

    def is_empty(self):
        return len(self.data) == 0
    
    def top(self):
        if self.is_empty():
            raise EmptyException("oops stack empty")
        return self.data[-1] # LIFO

    def pop(self):
        if self.is_empty():
            raise EmptyException("oops stack empty")
        popped = self.top()
        self.data = self.data[:-1]
        return popped

    def push(self, val):
        self.data.append(val)

    def min(self):
        temp_stack = Stack([])
        top_item = self.pop()
        while not self.is_empty():
            print(self.data)
            if temp_stack.is_empty():
                temp_stack.push(top_item)
            else:
                if temp_stack.top() > top_item:
                    temp_stack.push(top_item)
            top_item = self.pop()
        return temp_stack.top()

# Time: O(n)
# Space: O(n)        
    
import unittest

my_stack = Stack([])
class TestSum(unittest.TestCase):
    def test_solve(self):
        for item in [3, 4, 5, 9, 10, 3, 6, 0, 7, 188, 66, -1, 8, 90]:
            my_stack.push(item)
        self.assertEqual(my_stack.min(), -1)
        for item in [-1, -1, -100]:
            my_stack.push(item)
        self.assertEqual(my_stack.min(), -100)

if __name__ == '__main__':
    unittest.main()