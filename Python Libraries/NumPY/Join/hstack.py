# joins the arrays in horizontal manner

'''
[row1 row2 row3]
[col1 col2 col3]
'''
import numpy as np
n = np.array([[3,5,5],[4,3,9]])
n1 = np.array([[10,20,40],[12,19,29]])
n2 = np.array([[1,3,4],[4,0,0]])


n3 = np.hstack((n,n1,n2))
print(n3)
print(type(n3))
print(n3.ndim)
print(n3.shape)
