import numpy as np
arr_1d = np.array([1,2,3,4,5]);
print(arr_1d);
print(type(arr_1d));
# list vs numpy array
print(arr_1d*2)
import time 
start = time.time()
arr_1d = np.array([1,2,3,4,5])*100000000
print(arr_1d);
print(time.time()-start);
abhi = np.zeros((3,4))
print(abhi);
ones = np.ones((3,4));
print(ones);
full = np.full((2,2), 5)
print(full);
random = np.random.random((2,2))
print(random);
sequence = np.arange(0, 11, 2)
print(sequence);

# Vector, Matrix and Tensor

vector = np.array([1,2,3])
matrix = np.array([[1,2,3],[4,5,6]])
tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("vector",vector, "\n","matrix", matrix, "\n","tensor", tensor)

# Array Properties
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
print(arr.nbytes)

# Array Reshaping

arr = np.arange(1, 10)
print(arr)
reshaped_arr = arr.reshape(3, 3)
print(reshaped_arr)
flattened = reshaped_arr.flatten()
print(flattened)

ravled = reshaped_arr.ravel();
print(ravled);
# ravel (return view, instead of copy)

# Transpose
transposed = reshaped_arr.T
print(transposed)