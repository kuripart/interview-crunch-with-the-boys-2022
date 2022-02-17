# Author: Nithin Prasad
# Problem: CTCI Arrays and Strings, Problem 1
# Description: Is_Unique - Determine if string has all unique characters

def is_unique(inp_str):
    '''
    Input: inp_str
    Output: boolean says if string has unique characters/not
    '''
    chars_dict = {}

    #iterate through string and count character frequency dict
    for char in inp_str:

        if char not in chars_dict:
            chars_dict[char] = 1

        else:
            chars_dict[char] += 1

    #check if any chars are > 1 in frequency
    for char_key in chars_dict.keys():

        if chars_dict[char_key] > 1:
            return False

    return True

################### HINTS/OPTIMIZATIONS FOR is_unique #####################
# (1) Ask if ASCII or Unicode
# (2) Array of Booleans would explicitly make it O(c)
# (3) LOSE 1 LOOP!!!! could return False in the first loop right away!
# (4) Can use Bit Vectors like an integer to reduce space (eg.int stores 32 bits
       #... works for case if input reduced to just a-z

def is_unique_no_structs(inp_str):
    '''
    Same solution as above but without using additional data structures
    '''

    #Simulate C
    list_str = list(inp_str)

    #NOTE: we cannot use a list, string, dict, tuple etc to process this

    len_str = len(list_str)

    #Outer loop to go through full string
    for i in range(len_str):
        char_str = list_str[i]

        #Inner loop to go through remaining substring + checking for repetition
        for j in range(i+1,len_str):
            char_substr = list_str[j]

            if char_str == char_substr:
                return False

    return True

################### HINTS/OPTIMIZATIONS FOR is_unique_no_structs #####################
# (1) Can use n*log(n) sort eg. quicksort to sort in place and compare neighbours
  # ... this results in n*log(n) algorithm in average case!

if __name__ == "__main__":

    print(is_unique("")) #Size zero string is unique
    print(is_unique("a")) #single character is unique
    print(is_unique("alpha")) #Repetition of exact same character not unique
    print(is_unique("Alpha")) #Case-sensitive

    print("--------------------")

    print(is_unique_no_structs(""))
    print(is_unique_no_structs("a"))
    print(is_unique_no_structs("alpha"))
    print(is_unique_no_structs("Alpha"))
    
