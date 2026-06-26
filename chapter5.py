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
