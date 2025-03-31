# joins the arrays vertically
'''
row_1
col_1
row_2
col_2
row_3
col_3
row_4
col_4
'''
import numpy as np
n1 = np.array([[10,20,40],[12,19,29]])
n2 = np.array([[1,3,4],[4,0,0]])
n = np.array([[3,5,5],[4,3,9]])
n3 = np.vstack((n1,n2,n))
print(n3)
print(type(n3))
print(n3.ndim)
print(n3.shape)