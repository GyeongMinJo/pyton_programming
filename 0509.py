#import sys
#print(sys.builtin_module_names)

import numpy as np
import math
from math import gcd, fsum

print(gcd(10,20))
print(fsum([1,2,3]))

print(math.ceil(5.333))
#print(math.fsum([1,2,3]))
#print(math.gcd(10,20)) 
 
arrA = np.array([1,2,3,4,5])
arrB = np.array([6,7,8,9,10])

print(arrA + arrB)
print(arrA * arrB)
print(arrA / arrB)
print(arrA - arrB)

import hello  as h
print("==================")
h.helloworld()

print("__name__ in 0509.py",__name__)

