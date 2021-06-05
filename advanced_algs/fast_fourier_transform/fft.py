import numpy as np
import math
from functools import reduce
 
 
def raiser(omega, power):
   if power == 0:
       return (1, 0)
   omegas = [omega] * power
   return reduce(lambda a, b: (a[0] * b[0], a[1]+b[1]), omegas)
 
 
def multiplyer(omega, nz):
   return (omega[0]*nz[0], omega[1]+nz[1])
 
def add(pn1, pn2):
   c1 = to_complex(pn1)
   c2 = to_complex(pn2)
   z = (c1[0] + c2[0], c1[1] + c2[1])
   return to_polar(z)
 
def subtract(pn1, pn2):
   c1 = to_complex(pn1)
   c2 = to_complex(pn2)
   z = (c1[0] - c2[0], c1[1] - c2[1])
   return to_polar(z)
 
def to_polar(n):
   r = math.sqrt(n[0]**2 + n[1]**2)
   if n[0] == 0:
       if n[1] < 0:
           return (r, -math.pi/2)
       else:
           return (r, math.pi/2)
   theta = math.atan2(n[1], n[0])
   return (r, theta)
 
def to_complex(pn1):
   return (pn1[0]*math.cos(pn1[1]), pn1[0]*math.sin(pn1[1]))
 
# O(nlogn) time to get points from coefficients or the other way
def fft(coefficients, omega, n, rev=False):
   if omega is None:
       omega = (1, 2*math.pi/n)
       if rev :
           omega = raiser((1, 2*math.pi/n), n-1)
   if n == 1:
       return coefficients
   c_e = []
   c_o = []
   for i, c in enumerate(coefficients):
       if i % 2 == 0:
           c_e.append(c)
       else:
           c_o.append(c)
   odds = fft(c_o, raiser(omega, 2), n //2, rev)
   evens = fft(c_e, raiser(omega, 2), n //2, rev)
   ans = [1]*n
   for j in range(n//2):
       if j != 0:
           z = multiplyer(raiser(omega, j), odds[j])
       else:
           z = odds[j]
       ans[j] = add(evens[j], z)
       ans[n//2+j] = subtract(evens[j],  z)
   return ans
 
 # O(nlogn) time to multiply polynomials
def polynomial_multiplication(n1, n2):
   pts_1 = fft(n1, None, len(n1), False)
   pts_2 = fft(n2, None, len(n2), False)
   pts = []
   for i, p in enumerate(pts_1):
       pts.append((p[0] * pts_2[i][0], p[1] + pts_2[i][1]))
 
   res = fft(pts, None, len(pts), True)
   return res
