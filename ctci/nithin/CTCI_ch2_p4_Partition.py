#Author: Nithin Prasad
#Problem: CTCI Linked Lists, Problem 4
#Description: partition a linked list of elements around a value x, such that
# all nodes with value < x appear before all nodes with value > x

class Node:

    def __init__(self,val):

        self.val = val
        self.nxt = None

def create_LL(inp_list):

    head = None

    if len(inp_list) == 0:
        return None

    curr = None

    for elem in inp_list:
        if head == None:
            head = Node(elem)
            curr = head
        else:
            new_node = Node(elem)
            curr.nxt = new_node
            curr = curr.nxt

    return head

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

def partition(head,x):

    print("x = ",x)

    #For no elements in list or 1 element in list
    if head == None or head.nxt == None:
        return head

    #Iterate through LL
    lead = head.nxt
    trail = head

    while lead != None:

        if lead.val < x:
            #detach lead and move it to the start of the list
            trail.nxt = lead.nxt
            lead.nxt = head
            head = lead

            #reset lead
            lead = trail.nxt

        else:
            lead = lead.nxt
            trail = trail.nxt

    return head

######################### NOTES #####################
# (1) Can try 2 different linked lists (for < or > than) IF order is important ..

if __name__ == "__main__":

    #LL size 0
    print("")
    print("---------------------")
    LL = None
    print_LL(LL)
    LL_mod = partition(LL,3)
    print_LL(LL_mod)


    #LL size 1
    print("")
    print("---------------------")
    LL = create_LL([15])
    print_LL(LL)
    LL_mod = partition(LL,3)
    print_LL(LL_mod)

    #Linked list with x as 1 of elements in list
    print("")
    print("---------------------")
    LL = create_LL([5,4,3,2,1])
    print_LL(LL)
    LL_mod = partition(LL,4)
    print_LL(LL_mod)

    print("")
    print("---------------------")
    LL = create_LL([5,4,3,2,1])
    print_LL(LL)
    LL_mod = partition(LL,3)
    print_LL(LL_mod)

    print("")
    print("---------------------")
    LL = create_LL([5,4,3,2,1])
    print_LL(LL)
    LL_mod = partition(LL,2)
    print_LL(LL_mod)

    #Linked list with x outside of scope of elems in list
    print("")
    print("---------------------")
    LL = create_LL([5,4,3,2,1])
    print_LL(LL)
    LL_mod = partition(LL,6)
    print_LL(LL_mod)

    print("")
    print("---------------------")
    LL = create_LL([5,4,3,2,1])
    print_LL(LL)
    LL_mod = partition(LL,0)
    print_LL(LL_mod)


    
