def print_8_queens(board = [[None]*8]*8, num_left = 8, cache=set(), num_ans=[0]):
    if str(board) in cache:
        return
    else:
        cache.add(str(board))
    if num_left == 0:
        num_ans[0] += 1
        print("--------")
        for row in board:
            print(row)
        print("--------")
    for row_num, row in enumerate(board):
        for col_num, val in enumerate(row):
            if val is None:
                new_board = [r[:] for r in board]
                for col_numz, _ in enumerate(new_board[row_num]):
                    new_board[row_num][col_numz] = '-'
                for row in new_board:
                    row[col_num] = '-'
                i = row_num
                j = col_num
                while i <= len(new_board) - 1 and j <= len(new_board[0]) - 1:
                    new_board[i][j] = '-'
                    i += 1
                    j += 1
                i = row_num
                j = col_num
                while i >= 0 and j >= 0:
                    new_board[i][j] = '-'
                    i -= 1
                    j -= 1
                i = row_num
                j = col_num
                while i >= 0 and j >= 0 and i <= len(new_board) - 1 and j <= len(new_board[0]) - 1:
                    new_board[i][j] = '-'
                    i += 1
                    j -= 1
                i = row_num
                j = col_num
                while i >= 0 and j >= 0 and i <= len(new_board) - 1 and j <= len(new_board[0]) - 1:
                    new_board[i][j] = '-'
                    i -= 1
                    j += 1
                new_board[row_num][col_num] = 'Q'
                print_8_queens(new_board, num_left-1, num_ans=num_ans)
    return