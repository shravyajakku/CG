#Print array values with precision 3:

import numpy as np
np.random.seed(12)
arr1 = np.random.rand(10)
print("Original array elements:")
print(arr1)
print("Print array values with precision 3:")
print(arr1.round(3))