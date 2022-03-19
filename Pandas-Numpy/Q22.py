#to create an array of (3, 4) shape, multiply every elementvalue by 3 and display the new array.

import numpy as np

arr = np.arange(12).reshape(3, 4)
print("Original array elements:")
print(arr)
print("New array elements:")
new_arr = arr*3
print(new_arr)