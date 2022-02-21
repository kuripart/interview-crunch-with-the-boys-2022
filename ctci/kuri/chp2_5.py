class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next


def print_ll(root):
    '''
    print linked list please
    '''
    ans = ""
    temp = root
    while temp != None:
        ans += str(temp.val)
        temp = temp.next
    return ans



def solve(root1, root2):
    
    sum = 0 
    carry = 0
    ans = None
    temp = None

    while root1 != None or root2 != None:
        sum = carry
        if root1 != None:
            sum += root1.val
            root1 = root1.next

        if root2 != None:
            sum += root2.val
            root2 = root2.next

        carry = sum // 10
        sum = sum % 10
        
        sumnode = Node(sum, None)
        
        if temp == None:
            temp = ans = sumnode
        else:
            temp.next = sumnode
            temp = temp.next

    if carry:
        carrymnode = Node(carry, None)
        temp.next = carrymnode

    return print_ll(ans)


node1 = Node(1, None)
node2 = Node(2, None)
node3 = Node(3, None)
node4 = Node(4, None)
node5 = Node(5, None)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


node6 = Node(6, None)
node7 = Node(7, None)
node8 = Node(8, None)
node9 = Node(9, None)
node10 = Node(10, None)


node6.next = node7
node7.next = node8
node8.next = node9
# node9.next = node10


node11 = Node(11, None)
node12 = Node(12, None)
node13 = Node(13, None)
node14 = Node(14, None)

node11.next = node12
node12.next = node13
node13.next = node14

# Time: O(n)
# Space: O(n)

import unittest

class TestSum(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(node1, node6), '79146')
        self.assertEqual(solve(node1, node1), '246801')

if __name__ == '__main__':
    unittest.main()