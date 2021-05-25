# O(n^2) where n is length of string time and space
def longest_palindromic_subsequence(s):
   solutions = [[1 for _ in range(len(s))] for __ in range(len(s))]
   solutions[0][0] = 0
   for i in range(1,len(s)):
       solutions[0][i] = 1
       solutions[i][0] = 1
  
   longest_len = 0
   reversed_s = s[::-1]
   for i in range(1,len(s)):
       for j in range(1, len(s)):
           if i + j <= len(s):
               max_ = max(solutions[i-1][j], solutions[i][j-1], solutions[i-1][j-1])
               if max_ % 2 == 0 or s[i-1] == reversed_s[j-1]:
                   solutions[i][j] = max_ + 1
               else:
                   solutions[i][j] = max_
 
               if solutions[i][j] > longest_len:
                   longest_len = solutions[i][j]
           else:
               solutions[i][j] = 0
   return longest_len