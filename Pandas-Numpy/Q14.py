#find the set exclusive-or of two arrays.

import numpy as np

Array1 = np.array([0, 10, 20, 40, 60, 80])
Array2 = np.array([10, 30, 40, 50, 70])
print("Array1", Array1)
print("Array2", Array2)
print("Unique values that are in only one (not both) of the input arrays:")
print(np.setxor1d(Array1, Array2))
