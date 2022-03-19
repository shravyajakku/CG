#Q5
import numpy as np
Input_Array = np.ones([5, 5])
print(Input_Array)
print(" ------------ ")
Input_Array[1:-1, 1:-1] = 0
print(Input_Array)