#Author: Nithin Prasad
#Problem: CTCI Ch2 Linked Lists, Problem 7
#Description: given 2 singly linked lists, determine when they intersect. Intersection is
# defined by reference (not value).

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

def intersection(LL1,LL2):

    #If either LL is empty, return
    if LL1 == None or LL2 == None:
        return None

    #If either LL has length 1, both lists must be length 1
    if LL1.nxt == None and LL2.nxt == None:
        print("Lists of length 1")
        if LL1 == LL2:
            print("List nodes are equal")
            return LL1
        else:
            print("List nodes are not equal")
            return None
    
    #Obtain length of each list
    LL1_len = 0
    LL1_curr = LL1
    while LL1_curr != None:
        LL1_curr = LL1_curr.nxt
        LL1_len += 1

    LL2_len = 0
    LL2_curr = LL2
    while LL2_curr != None:
        LL2_curr = LL2_curr.nxt
        LL2_len += 1

    #Obtain bigger and smaller list, and the diff
    LL_big = None
    LL_small = None
    LL_size_diff = abs(LL1_len-LL2_len)
    if LL1_len >= LL2_len:
        LL_big = LL1
        LL_small = LL2
    else:
        LL_big = LL2
        LL_small = LL1

    #Check for first node equality

    LL_big_curr = LL_big
    LL_small_curr = LL_small
    tmp_size = LL_size_diff
    
    while LL_big_curr != None:

        if tmp_size == 0:
            #Then sublists from current node -> end of list are of same size
            if LL_small_curr == LL_big_curr:
                return LL_small_curr
            LL_small_curr = LL_small_curr.nxt
        else:
            #Only propogate big list pointer forward by 1 node
            tmp_size -= 1

        LL_big_curr = LL_big_curr.nxt

    #No match found
    return None

###################### NOTES ##############################
# 1) Algorithm takes O(A+B) time and O(1) space
# 2) Could use hash table but that takes more space

if __name__ == "__main__":

    #LL2 is empty
    print("")
    print("--------------")
    LL1 = create_LL([15])
    LL2 = None
    print_LL(LL1)
    print_LL(LL2)
    res = intersection(LL1,LL2)
    print_LL(res)

    #LL1 and LL2 have 1 node each but not the same node
    print("")
    print("--------------")
    LL1 = create_LL([15])
    LL2 = create_LL([15])
    print_LL(LL1)
    print_LL(LL2)
    res = intersection(LL1,LL2)
    print_LL(res)

    #LL1 and LL2 have 1 node each but IS pointing to same node
    print("")
    print("--------------")
    LL1 = create_LL([15])
    LL2 = LL1
    print_LL(LL1)
    print_LL(LL2)
    res = intersection(LL1,LL2)
    print_LL(res)

    #LL1 and LL2 have different length AND have intersection
    print("")
    print("--------------")
    LL1 = create_LL([15,11,13,18])
    LL2 = create_LL([9,11])
    LL2.nxt.nxt = LL1
    print_LL(LL1)
    print_LL(LL2)
    res = intersection(LL1,LL2)
    print_LL(res)

    #LL1 and LL2 have different length AND have NO intersection
    print("")
    print("--------------")
    LL1 = create_LL([15,11,13,18])
    LL2 = create_LL([9,11,19,21,23,25])
    print_LL(LL1)
    print_LL(LL2)
    res = intersection(LL1,LL2)
    print_LL(res)

    #LL1 and LL2 have same size and have intersection
    print("")
    print("--------------")
    LL1 = create_LL([15,11,13,18])
    LL2 = create_LL([19,21])
    LL2.nxt.nxt = LL1.nxt.nxt
    print_LL(LL1)
    print_LL(LL2)
    res = intersection(LL1,LL2)
    print_LL(res)

    #LL1 and LL2 have same length but no intersection
    print("")
    print("--------------")
    LL1 = create_LL([15,11,13,18])
    LL2 = create_LL([9,14,16,7])
    print_LL(LL1)
    print_LL(LL2)
    res = intersection(LL1,LL2)
    print_LL(res)
    
    
