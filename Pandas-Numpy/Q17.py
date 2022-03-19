#create a contiguous flattened array.

import numpy as np

arr = np.array([[10, 20, 30],[20, 40, 50]])
print("Original array:")
print(arr)
print("New Flattened Array:")
print(np.ravel(arr))