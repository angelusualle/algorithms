# O(n^1.6) time
def multiply(x,y):
   if x == 1:
       return y
   if y == 1:
       return x
   if y == 0 or x == 0:
       return 0
   bit_arr_x = []
   while x != 0:
       bit_arr_x.append(x & 1)
       x = x >> 1
   bit_arr_y = []
   while y != 0:
       bit_arr_y.append(y & 1)
       y = y >> 1
   while len(bit_arr_x) < len(bit_arr_y):
       bit_arr_x.append(0)
   while len(bit_arr_y) < len(bit_arr_x):
       bit_arr_y.append(0)
   if len(bit_arr_x) % 2 == 1:
       bit_arr_x.append(0)
       bit_arr_y.append(0)
   n = len(bit_arr_x) // 2
   bit_arr_x = bit_arr_x[::-1]
   bit_arr_y = bit_arr_y[::-1]
 
   bit_arr_x_l = bit_arr_x[:n]
   bit_arr_x_r = bit_arr_x[-n:]
   bit_arr_y_l = bit_arr_y[:n]
   bit_arr_y_r = bit_arr_y[-n:]
 
   x_r = convert_to_num(bit_arr_x_r[::-1])
   x_l = convert_to_num(bit_arr_x_l[::-1])
   y_r = convert_to_num(bit_arr_y_r[::-1])
   y_l = convert_to_num(bit_arr_y_l[::-1])
 
 
   p1 = multiply(x_l, y_l)
   p2 = multiply(x_r, y_r)
   p3 = multiply(x_r + x_l, y_r + y_l)
 
   return p1*2**(n*2) + (p3  - p1 - p2)*2**(n) + p2
 
 
def convert_to_num(bit_arr):
   n = 0
   while bit_arr:
       n = n << 1 | bit_arr.pop()
   return n
