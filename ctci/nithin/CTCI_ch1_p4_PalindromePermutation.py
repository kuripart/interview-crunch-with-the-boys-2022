#Author: Nithin Prasad
#Problem: CTCI Arrays and Strings, Problem 4
#Description: PalindromePermutation - determine if string is permutation of a
# palindrome.

def is_palindrome_perm(inp_str):
    '''
    Assume: any other punctuation treated as valid character
    Assume: case matters
    '''

    #Easy case: strings of length 0 or 1
    len_str = len(inp_str)
    if len_str == 0 or len_str == 1:
        return True

    chars_dict = {} #Each key is char, each value says is 1 if char frequency
                        # is odd or 0 if char frequency is even
    num_odds = 0 #Stores the number of odd numbered character frequencies

    #Harder case: loop through each character in string and determine
    # how many characters are 'odd' by the end
    for i in range(len_str):

        char = inp_str[i]

        #Ignore spaces and process character
        if char != " ":

            if char not in chars_dict:
                chars_dict[char] = 1
                num_odds += 1
            else:
                if chars_dict[char] == 1:
                    chars_dict[char] = 0
                    num_odds -= 1
                else:
                    chars_dict[char] = 1
                    num_odds += 1

    #Assess if number of odds is under 2, then we palindrome permutation exists
    if num_odds <= 1:
        return True
    else:
        return False


################# HINTS/OPTIMIZATIONS FOR PalindromePermutation ###############
# (1) Can save some space with Bit Vector and easily compute output with
#     bit manipulations

if __name__ == "__main__":

    #Test Cases
    print("",is_palindrome_perm("")) #True - Empty string IS a palindrome
    print("a",is_palindrome_perm("a")) #True - string of length 1 is a palindrome
    print("act coat",is_palindrome_perm("act coat")) #True - spaces don't matter
    print("Act coat",is_palindrome_perm("Act coat")) #False - case matters
    print("xaaaabbx",is_palindrome_perm("xaaaabbx")) #True
    
    
