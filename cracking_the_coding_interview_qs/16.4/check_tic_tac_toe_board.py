def check_win(board):
    cols = [[],[],[]]
    for row in board:
        if all([x=='x' for x in row]) or all([x=='o' for x in row]):
            return True
        for i, col in enumerate(row):
            cols[i].append(col)
    for col in cols:
        if all([x=='x' for x in col]) or all([x=='o' for x in col]):
            return True
    if all([x=='x' for x in [board[0][0], board[1][1], board[2][2]]]) or all([x=='o' for x in [board[0][0], board[1][0], board[2][2]]]):
        return True
    if all([x=='x' for x in [board[2][2], board[1][1], board[0][0]]]) or all([x=='o' for x in [board[2][2], board[1][0], board[0][0]]]):
        return True
    return False