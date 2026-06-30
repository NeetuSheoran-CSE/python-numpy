import numpy as np

arr = np.arange(1, 26).reshape(5, 5)
print(arr)

arr = np.arange(1, 26).reshape(5, 5)
print(arr[1:4, 1:4])

arr = np.array([1,2,3,4,5,6,7,8])

arr[arr % 2 == 0] = 0
print(arr)

arr = np.array([10,15,20,25,30,35])

even = np.sum(arr % 2 == 0)
odd = np.sum(arr % 2 != 0)

print("Even =", even)
print("Odd =", odd)

arr = np.array([10,20,30,40,50])

print(arr[::-1])

arr = np.array([12,45,99,23,87])

print(np.argmax(arr))


arr = np.array([12,45,99,23,87])

print(np.argmin(arr))

arr = np.array([[2,1,3],
                [1,0,2],
                [4,1,8]])

print("Determinant:")
print(np.linalg.det(arr))

print("Inverse:")
print(np.linalg.inv(arr))