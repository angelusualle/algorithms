# O(NM) time and O(1) space
def zero_matrix(matrix):
    n = len(matrix)
    if n == 0:
        return matrix
    m = len(matrix[0])
    first_row_has_zero = False
    first_column_has_zero = False
    for x in range(m):
        if matrix[0][x] == 0:
            first_row_has_zero = True
    for x in range(n):
        if matrix[x][0] == 0:
            first_column_has_zero = True
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for x in range(m):
        if matrix[0][x] == 0:
            for y in range(n):
                matrix[y][x] = 0
    for x in range(n):
        if matrix[x][0] == 0:
            for y in range(m):
                matrix[x][y] = 0
    if first_column_has_zero:
        for x in range(n):
            matrix[x][0] = 0
    if first_row_has_zero:
        for x in range(m):
            matrix[0][x] = 0
    return matrix
"""
# O(NM) time and O(N + M) space
def zero_matrix(matrix):
    if len(matrix) == 0:
        return matrix
    n = len(matrix)
    m = len(matrix[0])
    zero_rows = set()
    zero_columns = set()
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:
                zero_rows.add(i)
                zero_columns.add(j)
    for col in zero_columns:
        for x in range(n):
            matrix[x][col] = 0
    for row in zero_rows:
        for x in range(m):
            matrix[row][x] = 0
    return matrix
"""

"""
# O(NM) time and O(NM) space
def zero_matrix(matrix):
    new_matrix = [[None for x in row] for row in matrix]
    n = len(matrix)
    if n == 0:
        return matrix
    m = len(matrix[0])
    for i,row in enumerate(matrix):
        for j, val in enumerate(row):
            if new_matrix[i][j] is None:
                if val == 0:
                    for x in range(n):
                        new_matrix[x][j] = 0
                    for x in range(m):
                        new_matrix[i][x] = 0
                else:
                    new_matrix[i][j] = val
    return new_matrix
"""