#find common values between two arrays.

import numpy as np

Array1 = np.array([0, 10, 20, 40, 60])
print("Array1:", Array1)

Array2 = np.array([10, 30, 40])
print("Array2", Array2)

print("Common values between two arrays:")
print(np.intersect1d(Array1, Array2))