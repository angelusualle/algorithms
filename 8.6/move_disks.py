# O (2^n) time and O(n) space
def move_disks(n, start, buffer, end):
    if n <= 0:
        return
    move_disks(n - 1, start, end, buffer)
    end.append(start.pop())
    move_disks(n - 1, buffer, start, end)
