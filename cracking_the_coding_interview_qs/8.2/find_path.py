# O(n) runtime with memoization, O(n) space
def find_path(grid, r = 0, c = 0, cache = {}):
    if len(grid) == 0 or len(grid[0]) == 0:
        return False, None
    if grid[r][c] == 1:
        return False, None
    loc = [(r,c)]
    if loc[0] in cache:
        return cache[loc[0]]
    if r == len(grid) - 1 and  c == len(grid[0]) - 1:
        cache[loc[0]] = True, loc
        return True, loc
    if c < len(grid[0]) - 1:
        found, path = find_path(grid, r, c + 1)
        if found:
            loc.extend(path)
            cache[loc[0]] = True, loc
            return True, loc
    if r < len(grid) - 1:
        found, path = find_path(grid, r+1, c)
        if found:
            loc.extend(path)
            cache[loc[0]] = True, loc
            return True, loc
    return False, None

"""
# O(2^n) runtime, O(n) space
def find_path(grid, r = 0, c = 0):
    if len(grid) == 0 or len(grid[0]) == 0:
        return False, None
    if grid[r][c] == 1:
        return False, None
    loc = [(r,c)]
    if r == len(grid) - 1 and  c == len(grid[0]) - 1:
        return True, loc
    if c < len(grid[0]) - 1:
        found, path = find_path(grid, r, c + 1)
        if found:
            loc.extend(path)
            return True, loc
    if r < len(grid) - 1:
        found, path = find_path(grid, r+1, c)
        if found:
            loc.extend(path)
            return True, loc
    return False, None
"""