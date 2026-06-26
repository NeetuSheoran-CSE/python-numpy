#np.insert(array,index,value,axis=None)
# array - original array
# index - position where the new value will be inserted
# value - the value to be inserted
# axis - the axis along which to insert
# axis = 0, row-wise
# 1 column wise


#insert() - adds an element at a specified index in the array
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)
new_arr = np.insert(arr,2,100)
print(new_arr)

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d)
new_row = np.insert(arr_2d,1,[7,8,9],axis=0)
print(new_row)

#append() - adds an element to the end of the array
arr_2 = np.array([10,20,30])
print(arr_2)
new_arr_2 = np.append(arr_2,100)
print(new_arr_2)

#concatenate() - joins two or more arrays along an axis
#np.concatenate((arr1, arr2), axis=0)
#axis 0 > vertical stacking
#axis 1 > horizontal stacking

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
concatenated = np.concatenate((arr1, arr2), axis=0)
print(concatenated)

#delete() - removes an element at a specified index in the array
#np.delete(array,index,axis=None)
arr_3 = np.array([10,20,30,40,50])
print(arr_3)
new_arr_3 = np.delete(arr_3,2)
print(new_arr_3)

arr_2d = np.array([[1,2,3],[4,5,6]])
new=np.delete(arr_2d,0,axis=0)
print(new)

#stacking - combines multiple arrays into a single array
#vstack() - stacks arrays vertically (row-wise)
#hstack() - stacks arrays horizontally (column-wise)

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.stack((arr1,arr2))) #vertical stacking
print(np.hstack((arr1,arr2))) #horizontal stacking


#spliting - divides an array into multiple sub-arrays
#hsplit() - splits arrays horizontally (column-wise)
#vsplit() - splits arrays vertically (row-wise)

arr = np.array([[1,2,3,4],[5,6,7,8]])
print(np.hsplit(arr,2)) #horizontal split
print(np.vsplit(arr,2)) #vertical split
