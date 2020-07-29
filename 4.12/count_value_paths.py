from collections import defaultdict

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# O(n) worst time where each node is visited once in time complexity.
def count_value_paths(node, val):
    ans = [0]
    sums = defaultdict(int)
    count_value_paths_recursive(node, sums, 0, val, ans)
    return ans
def count_value_paths_recursive(node, sums, running_sum, val, ans):
    if node is None:
        return
    total = running_sum + node.data
    delta = total - val
    if delta == 0:
        ans[0] += 1
    if delta in sums:
        ans[0] += sums[delta]
    sums[total] += 1
    count_value_paths_recursive(node.left, sums, total, val, ans)
    count_value_paths_recursive(node.right, sums, total, val, ans)
    sums[total] -= 1
    

"""
# O(nlog(n)) time in balanced tree and O(n^2) in worst case if depth = number of nodes
def count_value_paths(node, val, ans=[0], parent_sums=[]):
    if node is None:
        return
    if node.data == val:
        ans[0] += 1
    for parent_sum in parent_sums:
        if node.data + parent_sum == val:
            ans[0] += 1
    for i in range(len(parent_sums)):
        parent_sums[i] += node.data
    parent_sums.append(node.data)
    count_value_paths(node.left, val, ans, parent_sums[:])
    count_value_paths(node.right, val, ans, parent_sums[:])
    return ans
"""