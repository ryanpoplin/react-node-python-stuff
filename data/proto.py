# News Articles Data Analysis:
# visited articles, dates/times, categories, time spent on those articles...
import numpy as np
p = np.array([48.858598, 2.294495])
print(p)
print(p.ndim) # getting the deminsion of array p
print(p.shape) # getting size of each array dimension
print(len(p)) # getting deminsion length of array p
print(p.dtype) # getting the data type of array p

# array type casting
a = np.array([1, 2, 3, 4])
print(a.dtype)
float_b = a.astype(np.float64) # convert our 'int64' array into 'float64'
print(float_b.dtype) # this refers to a 'copy' of the values of the previous array.

print(np.empty([3, 2], dtype = np.float64))
