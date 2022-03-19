#change the data type of an array.

import numpy as np

arr = np.array([[2, 4, 6], [6, 8, 10]])
print(arr)
print("Data type of the array x is:", arr.dtype.name)
print("New Type: float64")
print(arr.astype(float))