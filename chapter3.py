#indexing and slicing


# array[index]  1d array
#array[row,column] 2d array

import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[1]) 
print(arr[-1])

#slicing(start:stop:step)
# arr[start:end], start to end -1

print(arr[1:4:2])
print(arr[:3])
print(arr[::2])
print(arr[::-1])


#fancy indexing -- selectinf multiple elements at once 

arr = np.array([10,20,30,40,50])
print(arr[[0,2,4]])  # as a list paas karna h 


#filtering data with boolean masking
arr = np.array([10,20,30,40,50])
print(arr[arr>25])

#reshaping and manipulating arrays
#reshape(rows,columns) specify new shape 
#id dimension array ko reshape karna h to new shape specify karna h
arr = np.array([1,2,3,4,5,6])
print(arr.reshape(2,3))
print(arr.T)  # transpose   

#flattening arrays
#ravel() or flatten() 1d array me convert karna h
#.ravel() ->view
#.flatten() -> copy
arr = np.array([[1,2,3],[4,5,6]])
print(arr.ravel())
print(arr.flatten())
