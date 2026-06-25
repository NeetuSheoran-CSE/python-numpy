import numpy as np  

temperature = np.array([30, 32, 28, 35, 31])
average = np.mean(temperature)
print(average)


#1. speed
#2. less memory
#3. easy math operations

import numpy as np
python_list = [1,2,3,4,5]
print(python_list)

import numpy as np
numpy_array = np.array([1, 2, 3, 4, 5])
print(numpy_array)



#1D array
import numpy as np
ar_1d = np.array([1, 2, 3, 4, 5])
print(ar_1d)

#2D array
import numpy as np
arr_2d= np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)   

#multi-dimensional array
import numpy as np
matrix = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
print(matrix)

#creating arrays from python lists
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#with default values
import numpy as np
zeros_array = np.zeros(3)
print(zeros_array)


#ones(shape)
import numpy as np
ones_array = np.ones((2, 3))
print(ones_array)

#full(shape, value)
import numpy as np
full_array = np.full((2, 3), 7)
print(full_array)

#creation sequenves of numbers in numpy
#arange(start, stop, step)
import numpy as np
arr = np.arange(1,10,2)
print(arr)

#creating identity matrices
import numpy as np
identity_matrix = np.eye(4)
print(identity_matrix)

