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
    # while(left_index < right_index):
    #     if ll_value_list[left_index] != ll_value_list[right_index]:
    #         return False
    #     left_index += 1
    #     right_index -= 1

    # return True
    return ll_value_list == ll_value_list[::-1]
    
def create_ll(int_list):
    list_size = len(int_list)

    if list_size < 1:
        return None

    head = Node(int_list[0], None)
    prev = head

    for element in int_list[1:]:
        new_node = Node(element, None)
        prev.next = new_node

    return head


# Time: O(n)
# Space: O(n)

class TestDeleteMiddle(unittest.TestCase):
    def test_solve(self):
        head = create_ll([1,2,3,3,2])
        self.assertEqual(is_palindrome(head), False)
        self.assertEqual(is_palindrome(head.next), True)
        head = create_ll([])
        self.assertEqual(is_palindrome(head), True)
        head = create_ll([1])
        self.assertEqual(is_palindrome(head), True)
        head = create_ll([1,2,1])
        self.assertEqual(is_palindrome(head), True)

if __name__ == '__main__':
    unittest.main()