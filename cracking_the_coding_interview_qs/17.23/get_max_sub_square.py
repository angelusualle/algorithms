# O(N^2) get max subsquare
def get_max_sub_square(matrix):
    max_sq_area = 0
    max_sq_pts = None
    for ir, row in enumerate(matrix):
        for ic, val in enumerate(row):
            if val == 'w':
                continue
            diag = [ir, ic]
            while diag[0]+1 < len(matrix) and diag[1]+1 < len(matrix) and matrix[diag[0]+1][diag[1]+1] == 'b':
                diag[0] += 1
                diag[1] += 1
            z = ir
            while z < len(matrix) and matrix[z][ic] == 'b':
                z += 1
            max_d = z - ir - 1
            z = ic
            while z < len(matrix) and matrix[ir][ic] == 'b':
                z += 1
            max_w = z - ir - 1      
            while diag[0] >= ir and diag[1] >= ic:
                if diag[0] > max_d + ir:
                    diag[0] -= 1
                    diag[1] -= 1
                    continue
                if diag[1] > max_w + ic:
                    diag[0] -= 1
                    diag[1] -= 1
                    continue
                left = diag[1]
                while left != ic:
                    if matrix[diag[0]][ic] == 'b':
                        left -= 1
                    else:
                        left = -1
                        break
                if left == -1:
                    diag[0] -= 1
                    diag[1] -= 1
                    continue
                up = diag[0]
                while up != ir:
                    if matrix[up][diag[1]] == 'b':
                        up -= 1
                    else:
                        up = -1
                        break
                if up == -1:
                    diag[0] -= 1
                    diag[1] -= 1
                    continue
                if (up - ir + 1)**2 > max_sq_area:
                    max_sq_area = (up - ir + 1)**2
                    max_sq_pts = [(ir, ic), (diag[0], diag[1])]
                break
    return max_sq_pts