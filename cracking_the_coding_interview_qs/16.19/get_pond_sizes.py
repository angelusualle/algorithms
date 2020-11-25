# O(N) time, where n is size of pond, O(N) space since saving sizes
def get_pond_sizes(mat):
    sizes = []
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if val == 0:
                sizes.append(get_pond_size(mat, i, j))
    return sizes


def get_pond_size(mat, i, j):
    if i < 0 or i >= len(mat) or j < 0 or len(mat) < 1 or j >= len(mat[0]):
        return 0
    if mat[i][j] != 0:
        return 0
    size = 1
    mat[i][j] = -1
    size += get_pond_size(mat, i + 1, j)
    size += get_pond_size(mat, i - 1, j)
    size += get_pond_size(mat, i, j + 1)
    size += get_pond_size(mat, i, j - 1)
    size += get_pond_size(mat, i + 1, j + 1)
    size += get_pond_size(mat, i + 1, j - 1)
    size += get_pond_size(mat, i - 1, j + 1)
    size += get_pond_size(mat, i - 1, j - 1)
    return size
