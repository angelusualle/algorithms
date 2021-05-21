# O(nW)
def knapsack_with_repetition(w, v, W):
   values = []
   for i in range(W+1):
       max_val = 0
       for j,wt in enumerate(w):
           if wt <= i:
               if v[j] + values[i-wt] > max_val:
                   max_val = v[j] + values[i-wt]
       values.append(max_val)
   return values[-1]