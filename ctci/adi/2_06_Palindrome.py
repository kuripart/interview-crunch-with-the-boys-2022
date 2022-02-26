# Palindrome: Implement a function to check if a linked list is a palindrome.

import unittest

class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next

def print_ll(root):
    '''
    print linked list please
    '''
    temp = root
    while temp != None:
        print(temp.val)
        temp = temp.next

def is_palindrome(root):
    ll_value_list = []

    temp = root
    while(temp != None):
        ll_value_list.append(temp.val)
        temp = temp.next

    left_index = 0
    right_index = len(ll_value_list) - 1
    while(left_index < right_index):
        if ll_value_list[left_index] != ll_value_list[right_index]:
            return False
        left_index += 1
        right_index -= 1

    return True

node1 = Node(1, None)
node2 = Node(2, None)
node3 = Node(3, None)
node4 = Node(4, None)
node5 = Node(5, None)

def create_ll(n1=None, n2=None, n3=None, n4=None, n5=None):
    global node1, node2, node3, node4, node5
    node1 = Node(n1, None)
    node2 = Node(n2, None)
    node3 = Node(n3, None)
    node4 = Node(n4, None)
    node5 = Node(n5, None)
    
    if node1.val is None or node2.val is None:
        return
    node1.next = node2
    if node3.val is None:
        return
    node2.next = node3
    if node4.val is None:
        return
    node3.next = node4
    if node5.val is None:
        return
    node4.next = node5


# Time: O(n)
# Space: O(n)

class TestDeleteMiddle(unittest.TestCase):
    def test_solve(self):
        create_ll(1,2,3,3,2)
        self.assertEqual(is_palindrome(node1), False)
        self.assertEqual(is_palindrome(node2), True)
        create_ll()
        self.assertEqual(is_palindrome(node1), True)
        create_ll(1)
        self.assertEqual(is_palindrome(node1), True)
        create_ll(1,2,1)
        self.assertEqual(is_palindrome(node1), True)

if __name__ == '__main__':
    unittest.main()