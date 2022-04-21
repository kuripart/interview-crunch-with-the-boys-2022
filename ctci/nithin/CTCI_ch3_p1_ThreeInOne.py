#Author: Nithin Prasad
#Problem: CTCI Ch3 Stacks and Queues, Problem 1
#Description: implement 3 stacks using a fixed size array.

class Three_in_One:

    def __init__(self,arr_size):

        assert arr_size >= 3

        self.arr = [None]*arr_size
        self.lowerbounds = [0,int(arr_size/3),int(arr_size*2/3)]
        self.upperbounds = [int(arr_size/3)-1,int(arr_size*2/3)-1,arr_size-1]
        self.sp_list = [None,None,None]

    def print_arr(self):

        print("Array: ",self.arr)
        print("Array SP Lower Bounds: ",self.lowerbounds)
        print("Array SP Upper Bounds: ",self.upperbounds)
        print("sp_list: ",self.sp_list)

    def push_to_stack(self,stack,elem):

        assert stack == 1 or stack == 2 or stack == 3

        i = stack-1

        if self.sp_list[i] == None:
            self.sp_list[i] = self.lowerbounds[i]
            self.arr[self.sp_list[i]] = elem
        elif self.sp_list[i] == self.upperbounds[i]:
            print("No more space for stack 1. Push failed.")
        else:
            self.sp_list[i] += 1
            self.arr[self.sp_list[i]] = elem

    def pop_from_stack(self,stack):

        assert stack == 1 or stack == 2 or stack == 3

        i = stack-1

        if self.sp_list[i] == None:
            print("No elements remain in stack. Pop failed.")
        elif self.sp_list[i] == self.lowerbounds[i]:
            self.arr[self.sp_list[i]] = None
            self.sp_list[i] = None
        else:
            self.arr[self.sp_list[i]] = None
            self.sp_list[i] -= 1

################ NOTES ######################
# Follow up: what if you want more dynamic stack sizes?
# can we implement a solution? Pseudocode for moving stack boundaries?

if __name__ == "__main__":

    arr1 = Three_in_One(11)
    arr1.print_arr()
    arr1.push_to_stack(1,3)
    arr1.print_arr()
    arr1.push_to_stack(2,4)
    arr1.print_arr()
    arr1.push_to_stack(3,5)
    arr1.print_arr()
    arr1.push_to_stack(3,6)
    arr1.print_arr()
    arr1.push_to_stack(3,7)
    arr1.print_arr()
    arr1.push_to_stack(3,8)
    arr1.print_arr()
    arr1.push_to_stack(3,9)
    arr1.print_arr()
    arr1.pop_from_stack(3)
    arr1.print_arr()
    arr1.pop_from_stack(3)
    arr1.print_arr()
    arr1.pop_from_stack(3)
    arr1.print_arr()
    arr1.pop_from_stack(3)
    arr1.print_arr()
    arr1.pop_from_stack(3)
    arr1.print_arr()

            
                
        
        
