# O(nm)
def edit_distance(w1, w2):
   table = []
   for i in range(len(w1)):
       table.append([])
       for j in range(len(w2)):
           if i == 0:
               table[-1].append(j)
           elif j == 0:
               table[-1].append(i)
           else:
               table[-1].append(min(1+ table[i-1][j], 1 + table[i][j-1], int(w1[i] != w2[j]) + table[i-1][j-1]))
   return table[-1][-1]