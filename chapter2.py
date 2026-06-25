# how shape , size and type of numpy array can be checked?
# In NumPy, you can check the shape, size, and type of a NumPy array 
# usingthe following attributes and methods:
# shape: Returns the dimensions of the array    
# size: Returns the total number of elements in the array
# dtype: Returns the data type of the elements in the array


#********ATTRIBUTES ******

#shape --used when deal with multi-dimensional arrays
import numpy as np
arr_2d= np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.shape)  

#size --used to find the total number of elements in the array
import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1.size)

#ndim --used to find the number of dimensions of the array
import numpy as np
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_1d.ndim)   
print(arr_2d.ndim)  
print(arr_3d.ndim) 

#DTYPE --used to find the data type of the elements in the array

arr2 = np.array([10, 20, 30, 40, 50])
print(arr2.dtype)

#how to convert one data type into another data type in numpy array?
# Using astype() method

arr3 = np.array([12.3, 45.6, 67.8])
print(arr3.dtype)

int_arr = arr3.astype(int)
print(int_arr)
print(int_arr.dtype)


#math functions/operations in numpy
arr4 = np.array([10,20,30])
print(arr4 + 5)
print(arr4*2)
print(arr4 ** 2)


#aggregate functions in numpy
# data me se summary nikalna

