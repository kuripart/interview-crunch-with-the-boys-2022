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



def reverse(root):
    prev = None
    curr = root
    while curr != None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        

    print_ll(prev)



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
node9.next = node10


node11 = Node(11, None)
node12 = Node(12, None)
node13 = Node(13, None)
node14 = Node(14, None)

node11.next = node12
node12.next = node13
node13.next = node14


reverse(node1)