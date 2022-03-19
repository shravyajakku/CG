#remove specific elements in a numpy array.

import numpy as np

arr = np.linspace(10, 100, 10).astype(int)
print("Original array:")
print(arr)
print("Delete first", fourth and fifth elements:")
arr = np.delete(arr, [0, 3, 4])
print(arr)