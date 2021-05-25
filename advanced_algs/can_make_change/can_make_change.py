# O(nv) where n is length of denominations list and v is target value
def can_make_change(denominations, value):
   table = [[0 for _ in range(len(denominations))] for __ in range(value+1)]
   for i in range(len(denominations)):
       table[0][i] = True
   for i in range(1, value+1):
       for j in range(len(denominations)):
           if i - denominations[j] >= 0:
               with_ = table[i-denominations[j]][j]
           else:
               with_ = False
           if j >= 1:
               with_out = table[i][j-1]
           else:
               with_out = False
           table[i][j] = with_ or with_out
   return table[value][-1]