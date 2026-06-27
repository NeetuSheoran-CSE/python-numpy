#handling misssing and special values
#missing values can be handled in various ways, 
# such as removing them, imputing them with 
# mean/median/mode, or using algorithms that 
# can handle missing data.
#np.nan_to_num() can be used to replace NaN 
# with a specified value,
# and np.isnan() can be used to identify NaN 
# values in an array.
#np.isinf() can be used to check is any any value 
# is infinite like 10^1000
#np.nanmean() can be used to compute the mean 
# of an array while ignoring NaN values.
#NaN --not a number

#np.isnan(array)
import numpy as np
arr = np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))
print(np.nan == np.nan)

#nan_to_num()
arr=np.array([1,2,np.nan,4,np.nan,6])
cleaned_arr=np.nan_to_num(arr, nan=100)
print(cleaned_arr)

#np.isinf() -- 
arr = np.array([1,2,np.inf,4, -np.inf,6])
print(np.isinf(arr))
cleaned_arr = np.nan_to_num(arr, posinf=1000,neginf=1000)
print(cleaned_arr)