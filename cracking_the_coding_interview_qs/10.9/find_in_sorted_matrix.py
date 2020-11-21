# O(n)
def find_in_sorted_matrix(matrix, val):
    i = 0
    j = len(matrix[0]) - 1
    while ( i < len(matrix) and j >= 0 ): 
        if (matrix[i][j] == val ): 
            return (i,j)
        if (matrix[i][j] > val ): 
            j -= 1
        else:  
            i += 1
    return None