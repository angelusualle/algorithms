# O(K^2) time and space
def langston_ant(K):
    grid = [[] for _ in range(K)]
    alt = True
    black = True
    for i in range(K):
        if black:
            grid[i].append('b')
            black = False
            alt=True
        else:
            grid[i].append('w')
            black = True
            alt=False
        for j in range(K - 1):
            if alt:
                grid[i].append('w')
                alt = False
            else:
                grid[i].append('b')
                alt = True
    ant = [K // 2, K // 2, 'right']
    for i in range(K):
        if grid[ant[0]][ant[1]] == 'w':
            grid[ant[0]][ant[1]] = 'b'
            if ant[2] == 'right':
                ant[2] = 'down'
            elif ant[2] == 'down':
                ant[2] = 'left'
            elif ant[2] == 'left':
                ant[2] = 'up'
            else:
                ant[2] = 'right'
        else:
            grid[ant[0]][ant[1]] = 'w'
            if ant[2] == 'right':
                ant[2] = 'up'
            elif ant[2] == 'up':
                ant[2] = 'left'
            elif ant[2] == 'left':
                ant[2] = 'down'
            else:
                ant[2] = 'right'
        if ant[2] == 'right':
            ant[1] += 1
        elif ant[2] == 'down':
            ant[0] += 1
        elif ant[2] == 'left':
            ant[1] -= 1
        elif ant[2] == 'up':
            ant[0] -= 1
    for row in grid:
        print(row)
    return grid