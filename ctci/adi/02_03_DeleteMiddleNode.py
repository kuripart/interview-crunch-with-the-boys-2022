# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e- >f

# from pickle import NONE
# from venv import create
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

def sum_ll(root):
    '''
    return the sum of all elements of the ll
    '''
    sum = 0
    temp = root
    while temp != None:
        sum = sum + temp.val
        temp = temp.next
    return sum

def delete_middle_node(item_to_delete):
    if item_to_delete.next == None:
        print(f"LOL RIP!")
        return

    # can only delete middle elements
    next_item = item_to_delete.next
    item_to_delete.val = next_item.val
    item_to_delete.next = next_item.next

def create_ll():
    global node1, node2, node3, node4, node5
    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    node5 = Node(5, None)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5


# Time: O(1)
# Space: O(1)

class TestDeleteMiddle(unittest.TestCase):
    def test_solve(self):
        create_ll()
        delete_middle_node(node2)
        self.assertEqual(sum_ll(node1), 1+3+4+5)
        create_ll()
        delete_middle_node(node3)
        self.assertEqual(sum_ll(node1), 1+2+4+5)
        create_ll()
        delete_middle_node(node4)
        self.assertEqual(sum_ll(node1), 1+2+3+5)
        create_ll()
        delete_middle_node(node5)
        self.assertNotEqual(sum_ll(node1), 1+2+3+4)

if __name__ == '__main__':
    unittest.main()
