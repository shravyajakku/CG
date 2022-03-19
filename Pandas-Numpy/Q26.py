#to add an extra column to an numpy array.

import numpy as np

arr1 = np.arange(10, 70, 10).reshape(2,3)
print(arr1)
arr2 = np.array([100, 200]).reshape(2,1)
print(np.concatenate((arr1, arr2), axis=1))