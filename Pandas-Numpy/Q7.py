#Q7
import numpy as np
print("Checkerboard pattern:")
Input_Array = np.zeros((8,8),dtype=int)
Input_Array[1::2, ::2] = 1
Input_Array[::2, 1::2] = 1
print(Input_Array)