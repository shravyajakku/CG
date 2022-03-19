#convert a NumPy array into Python list structure.

import numpy as np

l = []

arr = np.arange(6).reshape(3, 2)
print("Original array elements:")
print(arr)
print("Array to list:")
for i in arr:
    l.append(list(i))
print(l)