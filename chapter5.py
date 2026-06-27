# broadcasting and vectorization

prices = [100,200,300]
discount = 10 #10% discount
final_prices=[]
for price in prices:
    final_price = price-(price*discount/100)
    final_prices.append(final_price)
print(final_prices)

import numpy as np
pricess = np.array([100,200,300])
discount = 10 #scalar single value
final_prices=pricess-(pricess*discount/100)
print(final_prices)

#single value - scalar
arr=np.array([100,200,300])
result=arr*2
print(result)

#2d array
arr_2d=np.array([[1,2,3],[4,5,6]])
vector=np.array([10,20,30])
result=arr_2d+vector
print(result)

#error

import numpy as np
# arr1=np.array([[1,2,3],[4,5,6]]) #shape(2,3)
# arr2=np.array([12,34]) #shape(2)
# result= arr1 + arr2
# print(result)

#reshape()

list1=[1,2,3]
list2=[4,5,6]
result = [x+y for x,y in zip(list1,list2)]
print(result)


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = arr1+arr2
print(result)

arr = np.array([10,20,30])
multiplied = arr*3
print(multiplied)

#boasting --expands smaller array to larger array
# faster than loop
# 1d--explands to 2d shape
#vectorization -- performing operations on entire arrays at once
#100* faster than for loop
#used in matrix operations, image processing, machine learning, deep learning



