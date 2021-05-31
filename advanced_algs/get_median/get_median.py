import random
 
 # O(n) average case, O(n^2) worst case
def get_median(arr,m=None):    
   smaller = []
   larger = []
   equal = []
   num = random.choice(arr)
   for n in arr:
       if n < num:
           smaller.append(n)
       elif n > num:
           larger.append(n)
       else:
           equal.append(n)
   if m is None:
       m  = len(arr) // 2 + 1
  
   if m > len(smaller) + len(equal):
       return get_median(larger, m - len(smaller) - len(equal))
   elif m <= len(smaller):
       return get_median(smaller, m)
   else:
       return equal[0]