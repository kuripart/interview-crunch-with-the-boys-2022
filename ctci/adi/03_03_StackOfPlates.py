# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific substack.

from dataclasses import dataclass
from math import ceil


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

@dataclass
class SetOfStacks:
    stack_set: list
    stack_height: int

    def __init__(self, stack_height):
        self.stack_height = stack_height
        self.stack_set = []
    
    def is_empty(self):
        return len(self.stack_set) == 0
    
    def top(self):
        if self.is_empty():
            raise EmptyException("oops stack empty")
        return self.stack_set[-1].top() # LIFO

    def pop(self):
        if self.is_empty():
            raise EmptyException("oops stack empty")
        popped = self.stack_set[-1].pop()
        if len(self.stack_set[-1].data) == 0:
            self.stack_set = self.stack_set[:-1]
        return popped

    def push(self, val):
        if self.is_empty():
            self.add_new_stack(val)
        elif len(self.stack_set[-1].data) >= self.stack_height:
            self.add_new_stack(val)
        else:
            self.stack_set[-1].push(val)

    def add_new_stack(self, val):
        new_stack = Stack([])
        new_stack.push(val)
        self.stack_set.append(new_stack)

    def get_stack_set_len(self):
        return len(self.stack_set)

    # Time: O(n)
    # Space: O(n)
    def pop_at(self, index):
        len_stack_set = self.get_stack_set_len()
        if index < len_stack_set:
            popped = self.stack_set[index].pop()
            rebalance_list = []
            while(index < self.get_stack_set_len()):
                rebalance_list.append(self.pop())

            for i in rebalance_list[::-1]:
                self.push(i)

            return popped
        raise LookupError(f"set of stacks goes only till {self.get_stack_set_len()}. Can not access index {index}")

       
    
import unittest

class TestSum(unittest.TestCase):
    def test_solve(self):
        # setup
        elements_to_push = [3, 4, 5, 9, 10, 3, 6, 0, 7, 188, 66, -1, 8, 90]
        stack_height = 3
        my_stack = SetOfStacks(stack_height)
        for item in elements_to_push:
            my_stack.push(item)
        
        self.assertEqual(my_stack.get_stack_set_len(), ceil(len(elements_to_push) / stack_height))
        self.assertEqual(my_stack.pop(), 90)
        self.assertEqual(my_stack.pop_at(2), 7)
        self.assertEqual(my_stack.pop_at(2), 188)
        self.assertEqual(my_stack.get_stack_set_len(), ceil(len(elements_to_push) / stack_height - 1))

if __name__ == '__main__':
    unittest.main()