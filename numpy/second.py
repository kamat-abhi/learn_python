# Numpy Array operation
import numpy as np
arr = np.array(range(1, 10))
print(arr[2:7])
print(arr[1:8:2])
print(arr[-3])

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(arr_2d[1,2])
print(arr_2d[1][1])
# both are valid but first one is prefered in numpy
print(arr_2d[1:3, 1:3])
print(arr_2d[:, 1]) #column target

# Sorting
unsorted = np.array([4,3,5,6,3,2,1,7,8,9]);
print(np.sort(unsorted));

arr__2d = np.array([[3,1], [1, 4], [2, 3]]);
print(np.sort(arr__2d, axis=0)); # sort by column
print(np.sort(arr__2d, axis=1)); # sort by row

# Filter
numbers = np.array(range(1, 11)); 
even_number = numbers[numbers % 2 == 0];
print(even_number);

# Filter with mask
mask = numbers % 2 == 0
print(numbers[mask]);

# Fancy indexing vs np.where()
indices = [0, 2, 4]
print(numbers[indices])

where_indices = np.where(numbers % 2 == 0)
print(numbers[where_indices])

condition_array = np.where(numbers>5, numbers*5, numbers);
print(condition_array);

