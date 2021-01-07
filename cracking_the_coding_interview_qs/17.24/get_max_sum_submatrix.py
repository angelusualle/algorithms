#(N^3) in nxn matrix
def get_max_sum_submatrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    best_one = None
    for i in range(len(matrix)):
        partial_sum = [0 for z in range(num_cols)]
        for j in range(i, num_rows):
            for z in range(num_cols):
                partial_sum[z] += matrix[j][z]
            start = 0
            sum_ = 0
            best = None
            for y in range(num_cols):
                sum_ += partial_sum[y]
                if best is None or sum_ > best[0]:
                    best = (sum_, start, y)
                if sum_ < 0:
                    start = y + 1
                    sum_ = 0
            if best_one is None or best[0] > best_one[0]:
                best_one = best
            
    return best_one
                
    