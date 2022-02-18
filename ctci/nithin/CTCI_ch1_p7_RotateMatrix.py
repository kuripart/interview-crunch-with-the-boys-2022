#Author: Nithin Prasad
#Problem: CTCI Arrays and Strings, Problem 7
#Description: RotateMatrix - given an image represented by NxN matrix, rotate
# the image by 90 degrees.

def rotate_matrix(matrix_in):
    '''
    Assume: clockwise rotation by 90 degrees
    '''
    #Handle edge cases:
    # (1) matrix has no elements (length is 0)
    # (2) first element of matrix has no elements (0x0 matrix)
    if len(matrix_in) == 0:
        return matrix_in
    if len((matrix_in[0])) == 0:
        return matrix_in

    len_matrix = len(matrix_in[0])

    #Create Hollow matrix_out
    matrix_out = []
    for i in range(len_matrix):
        row_of_zeros = [0]*len_matrix
        matrix_out.append(row_of_zeros)
    
    #Rotation Mechanism: Rows become Columns
    for i in range(len_matrix):
        for j in range(len_matrix):
            matrix_out[j][len_matrix-i-1] = matrix_in[i][j]

    return matrix_out

def rotate_matrix_inplace(matrix_in):
    '''
    Assume: clockwise rotation by 90 degrees
    '''
    
    #Handle edge cases:
    # (1) matrix has no elements (length is 0)
    # (2) first element of matrix has no elements (0x0 matrix)
    if len(matrix_in) == 0:
        return matrix_in
    if len((matrix_in[0])) == 0:
        return matrix_in

    len_matrix = len(matrix_in[0])
    index_max = len_matrix - 1

    #Rotation Mechanism: each layer is rotated independently
    depth = int(len_matrix/2) #for odd matrix length, keep inner elem static
    print("Depth: ",depth)

    for depth_i in range(depth):
        local_max = len_matrix - 2*depth_i - 1
        for local_j in range(local_max):
            temp = matrix_in[local_j+depth_i][index_max-depth_i] #Save Right to Temp
            matrix_in[local_j+depth_i][index_max-depth_i] = matrix_in[0+depth_i][local_j+depth_i] #Top to right
            matrix_in[0+depth_i][local_j+depth_i] = matrix_in[index_max-local_j-depth_i][0+depth_i] #Left to Top
            matrix_in[index_max-local_j-depth_i][0+depth_i] = matrix_in[index_max-depth_i][index_max-local_j-depth_i] #Bot to Left
            matrix_in[index_max-depth_i][index_max-local_j-depth_i] = temp #Temp to Bot

    return matrix_in

#################### TIPS TO SOLVE RotateMatrix #############################
# (1) For the optimized function - don't convert global coord to local to global again. Just work in global whole time.

if __name__ == "__main__":

    M = [] #Matrix without any elements
    print("---------------")
    print(M)
    M_out = rotate_matrix(M)
    M_out2 = rotate_matrix_inplace(M)
    print(M_out)
    print(M_out2)
    M = [[]] #Hollow nested matrix
    print("---------------")
    print(M)
    M_out = rotate_matrix(M)
    M_out2 = rotate_matrix_inplace(M)
    print(M_out)
    print(M_out2)
    M = [[3]] #1x1 matrix
    print("---------------")
    print(M)
    M_out = rotate_matrix(M)
    M_out2 = rotate_matrix_inplace(M)
    print(M_out)
    print(M_out2)
    M = [[1,2],[3,4]]
    print("---------------")
    print(M)
    M_out = rotate_matrix(M)
    M_out2 = rotate_matrix_inplace(M)
    print(M_out)
    print(M_out2)
    M = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print("---------------")
    print(M)
    M_out = rotate_matrix(M)
    M_out2 = rotate_matrix_inplace(M)
    print(M_out)
    print(M_out2)

    
    
