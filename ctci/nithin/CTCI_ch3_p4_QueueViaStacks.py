#Author: Nithin Prasad
#Problem: CTCI Ch3 Stacks and Queues, Problem 4
#Description: Implement a MyQueue class which implements a queue using 2
# stacks.

def print_LL(head):

    str_print = ""

    if head == None:
        print("None")

    else:
        
        curr = head

        while curr != None:
            str_print = str_print + str(curr.val) + " -> "
            if curr.nxt == None:
                str_print += "None"
            curr = curr.nxt

        print(str_print)

class Node:

    def __init__(self,val):
        self.val = val
        self.nxt = None

class Stack:

    def __init__(self):
        self.head = None

    def push(self,elem):
        newNode = Node(elem)

        if self.head == None:
            self.head = newNode
        else:
            newNode.nxt = self.head
            self.head = newNode

    def pop(self):
        if self.head == None:
            print("Empty stack")
            return None
        else:
            poppedNode = self.head
            self.head = self.head.nxt
            return poppedNode

    def peek(self):

        if self.head == None:
            return None

        return self.head.val

    def is_empty(self):
        return (self.head == None)

class MyQueue:

    def __init__(self):
        self.stackOne = Stack()
        self.stackTwo = Stack()
        self.queueSize = 0

    def push(self,elem):
        self.stackOne.push(elem)
        self.queueSize += 1

    def remove(self):

        if self.queueSize == 0:
            print("Empty queue")
            return None

        for i in range(self.queueSize):
            tmpNode = self.stackOne.pop()
            self.stackTwo.push(tmpNode.val)

        poppedNode = self.stackTwo.pop()

        self.queueSize -= 1

        for i in range(self.queueSize):
            tmpNode = self.stackTwo.pop()
            self.stackOne.push(tmpNode.val)

        return poppedNode

    def peek(self):

        for i in range(self.queueSize):
            tmpNode = self.stackOne.pop()
            self.stackTwo.push(tmpNode.val)

        retVal = self.stackTwo.peek()

        for i in range(self.queueSize):
            tmpNode = self.stackTwo.pop()
            self.stackOne.push(tmpNode.val)

        return retVal

    def isEmpty():

        return (self.queueSize == 0)

############################# NOTES ###############################
# 1) Can implement a stackNewest and stackOldest. This way allows us
#   to perform consecutive Oldest stack operations such as peek/remove
#   in constant time. Thus would only reverse the stack if we absolutely
#   need to!

if __name__ == "__main__":

    print("----------- STACK TESTING ------------")
    stack = Stack()
    print_LL(stack.head)
    stack.push(2)
    print_LL(stack.head)
    stack.push(3)
    print_LL(stack.head)
    stack.push(4)
    print_LL(stack.head)
    print(stack.peek())
    print(stack.pop().val)
    print_LL(stack.head)
    print(stack.pop().val)
    print(stack.pop().val)
    stack.pop()

    print("------------- QUEUE TESTING -----------")
    queue = MyQueue()
    print_LL(queue.stackOne.head)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    print_LL(queue.stackOne.head)
    print(queue.peek())
    print(queue.remove().val)
    print_LL(queue.stackOne.head)
    queue.remove()
    print_LL(queue.stackOne.head)
    queue.remove()
    print_LL(queue.stackOne.head)
    print(queue.peek())
    queue.remove()

    

        
