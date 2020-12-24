import heapq

# O(N + K*log(N)) where n is len of nums and k is number of smallest
def get_k_smallest(k, nums):
    heapq.heapify(nums)
    ans = []
    for _ in range(k):
        ans.append(heapq.heappop(nums))
    return ans