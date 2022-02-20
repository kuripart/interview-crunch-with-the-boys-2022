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



def solve(root, kth_to_last):
    ll_len = 0
    temp = root

    # find the length of the linked list: O(n)
    while temp != None:
        ll_len += 1
        temp = temp.next
    
    # move to the difference: O(n)
    temp2 = root
    for i in range(ll_len - kth_to_last - 1):
        temp2 = temp2.next

    return temp2.val


node1 = Node(1, None)
node2 = Node(2, None)
node3 = Node(3, None)
node4 = Node(4, None)
node5 = Node(5, None)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# Time: O(n)
# Space: O(1)

import unittest

class TestSum(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(node1, 1), 4)
        self.assertEqual(solve(node1, 2), 3)
        self.assertEqual(solve(node1, 3), 2)
        self.assertEqual(solve(node1, 4), 1)

if __name__ == '__main__':
    unittest.main()