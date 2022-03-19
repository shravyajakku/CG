#Q6
import numpy as np
Input_Array = np.ones((3,3))
print(Input_Array)
print("0 on the border and 1 inside in the array")
Input_Array = np.pad(Input_Array, pad_width=1, mode='constant', constant_values=0)
print(Input_Array)