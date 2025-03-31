# joins the columns together

import numpy as np
n1 = np.array([1,2,3]) 
n2 = np.array([10,20,30])


n = np.column_stack((n1,n2))
print(n)
print(type(n))
print(n.ndim)
print(n.shape)