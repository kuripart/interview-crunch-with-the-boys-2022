#Author: Nithin Prasad
#Problem: CTCI Ch4 Trees and Graphs, Problem 4
#Description: Given a binary tree, check if its balanced (if the height of subtrees at
#  any given nodes do not differ by more than 1.

class Result:

    def __init__(self):
        self.result = True

class BTNode:

    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.head = None

    def print_tree(self):
        print("Printing Tree")

        nodes = [self.head]

        while len(nodes) > 0:
            node_row = ""
            new_nodes = []
            for node in nodes:
                if node != None:
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
                    node_row = node_row + " " + str(node.val)
                else:
                    node_row = node_row + " None"
            nodes = new_nodes[:]
            print(node_row)

def check_balanced(tree):

    res = Result()

    #Note: this function also handles empty trees (height 0)
    height = cb_helper(tree.head,res)

    return res.result

def cb_helper(node,res):

    #Base Case
    if node == None:
        return 0

    h_left = cb_helper(node.left,res)

    h_right = cb_helper(node.right,res)

    if res.result == True:
        if abs(h_left-h_right) > 1:
            res.result = False        

    return max(h_left,h_right)+1 

################################# NOTES ###################################
# 1) Could be optimized using a checkHeight function to do both the height check
#     and the balancing! Just return/propagate an error code if tree/subtrees are
#     unbalanced. Let the main function take care of the boolean return.
# 2) Function should run in O(n) time and O(log n = h) space. O(h) space since at
#     any time, there are h calls on stack (at maximum) for recursive function call stack.
        
if __name__ == "__main__":

    bTreeA = BinaryTree()
#    bTreeA.head = BTNode(3)
#    bTreeA.head.left = BTNode(4)
#    bTreeA.head.right = BTNode(5)
#    bTreeA.head.left.left = BTNode(6)
    bTreeA.print_tree()

    print(check_balanced(bTreeA))
    

