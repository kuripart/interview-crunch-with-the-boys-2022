#Author: Nithin Prasad
#Problem: CTCI Arrays and Strings, Problem 7
#Description: RotateMatrix - given an image represented by NxN matrix, rotate
# the image by 90 degrees.


class Node:

    def __init__(self,val_in):
        self.val = val_in
        self.nxt = None

def print_LL(head):

    str_print = ""

    if head == None:
        print("None")

    curr = head

    while curr != None:
        str_print = str_print + str(curr.val) + " -> "
        if curr.nxt == None:
            str_print += "None"
        curr = curr.nxt

    print(str_print)
    
def remove_dups(head_node):
    '''
    Time complexity: O(n^2)
    Space complexity: O(1)
    '''

    #0 element case
    if head_node == None:
        return None

    #1 element case
    if head_node.nxt == None:
        return head_node

    #More than 1 element ...
    curr = head_node #Tracks the node that is currently being compared to
    lead = None #Runs through the rest of the LL
    follow = None #Follows the lead by 1 node from behind ...

    while curr != None:
        #print("In Outer Loop")
        #print_LL(head_node)

        lead = curr.nxt
        follow = curr

        while lead != None:
            if curr.val == lead.val:
                #print("In IF")
                #print_LL(head_node)
                follow.nxt = lead.nxt #Delete lead from LL
                lead = lead.nxt
                #print_LL(head_node)
            else:
                lead = lead.nxt
                follow = follow.nxt

        #print("Curr: ", curr)
        curr = curr.nxt

    return head_node

######################### NOTES #####################
# (1) Above solution runs in O(n^2) without auxiliary space. However it is INEFFICIENT!
# => try a HASH TABLE!

def remove_dups_optimal_time(head_node):

    #0 element case
    if head_node == None:
        return None

    #1 element case
    if head_node.nxt == None:
        return head_node

    value_table = {}

    value_table[head_node.val] = 1
    lead = head_node.nxt
    trail = head_node

    while lead != None:

        if lead.val in value_table:
            trail.nxt = lead.nxt
            lead = lead.nxt
        else:
            value_table[lead.val] = 1
            lead = lead.nxt
            trail = trail.nxt

    return head_node

if __name__ == "__main__":

    #Empty LL case
    print("-------------------------")
    LL = None
    print_LL(LL)
    print(".. remove dups ..")
    print_LL(remove_dups_optimal_time(LL))

    #Single elem LL case
    print("-------------------------")
    LL = Node(3)
    print_LL(LL)
    print(".. remove dups ..")
    print_LL(remove_dups_optimal_time(LL))

    #adjacent duplicates
    print("-------------------------")
    LL = Node(3)
    LL.nxt = Node(3)
    print_LL(LL)
    print(".. remove dups ..")
    print_LL(remove_dups_optimal_time(LL))

    #palindromic duplicates
    print("-------------------------")
    LL = Node(3)
    LL.nxt = Node(4)
    LL.nxt.nxt = Node(5)
    LL.nxt.nxt.nxt = Node(4)
    LL.nxt.nxt.nxt.nxt = Node(3)
    print_LL(LL)
    print(".. remove dups ..")
    print_LL(remove_dups_optimal_time(LL))

    #multiple repeated duplicates
    print("-------------------------")
    LL = Node(3)
    LL.nxt = Node(4)
    LL.nxt.nxt = Node(3)
    LL.nxt.nxt.nxt = Node(4)
    LL.nxt.nxt.nxt.nxt = Node(5)
    LL.nxt.nxt.nxt.nxt.nxt = Node(2)
    LL.nxt.nxt.nxt.nxt.nxt.nxt = Node(3)
    LL.nxt.nxt.nxt.nxt.nxt.nxt.nxt = Node(3)
    LL.nxt.nxt.nxt.nxt.nxt.nxt.nxt.nxt = Node(6)
    LL.nxt.nxt.nxt.nxt.nxt.nxt.nxt.nxt.nxt = Node(6)
    LL.nxt.nxt.nxt.nxt.nxt.nxt.nxt.nxt.nxt.nxt = Node(2)
    print_LL(LL)
    print(".. remove dups ..")
    print_LL(remove_dups_optimal_time(LL))










    



    
