# O(n) time where n is number of bars and O(1) space
def max_area(height):
    i = 0
    j = len(height) - 1
    area = 0
    while i != j:
        if min(height[j], height[i]) * (j - i) > area:
            area = min(height[j], height[i]) * (j - i)
        if height[j] > height[i]:
            i += 1
        else:
            j -= 1
    return area