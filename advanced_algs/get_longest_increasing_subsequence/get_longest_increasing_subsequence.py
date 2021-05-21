# O(n^2) overall
def get_longest_increasing_subsequence(nums):
   l = len(nums)
   # reverse adjacency list O(n^2)
   reverse_adjacency = {i:set() for i in range(l)}
   for i,n in enumerate(nums):
       for j,e in enumerate(nums[i+1:], i +1):
           if n < e:
               reverse_adjacency[j].add(i)
 
   # dynamic programming O(V+E)
   p = ['-']*l
   max_len = [0]*l
   best_max = (0,0) # (len, index)
   for i in range(l):
       if len(reverse_adjacency[i]) != 0:
           maxz = float('-inf')
           for c in reverse_adjacency[i]:
               if max_len[c] > maxz:
                   max_i = c
           max_ = 1 + max_len[max_i]
       else:
           max_i = '-'
           max_ = 1
       p[i] = max_i
       max_len[i] = max_
       if max_ > best_max[0]:
           best_max = (max_, i)
   path = [best_max[1]]
   while path[-1] != '-':
       path.append(p[path[-1]])
   return path, best_max[0]