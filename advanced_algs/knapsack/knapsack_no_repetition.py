# O(nW)
def knapsack_no_repetition(w, v, W):
   table = []
   l = len(w)
   for i in range(l + 1):
       table.append([])
       for cap in range(W+1):
           if i == 0 or cap == 0:
               table[-1].append(0)
           else:
               if w[i-1] > cap:
                   table[-1].append(table[i-1][cap])
               else:
                   table[-1].append(max(table[i-1][cap], v[i-1] + table[i-1][cap-w[i-1]]))
   return table[-1][-1]