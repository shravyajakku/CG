#concatenate two 2-dimensional arrays.

import numpy as np

Array1 = np.array([[0, 1, 3], [5, 7, 9]])
Array2 = np.array([[0, 2, 4], [6, 8, 10]])
concat_array = np.concatenate((Array1, Array2), axis=1)
print(concat_array)