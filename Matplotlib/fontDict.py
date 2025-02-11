import matplotlib.pyplot as plt
import numpy as np
x = np.array([2,3,5,6,9])
y = np.array([1,5,6,9,10])

font1 = {"family":"serif","color":"red","size":20}
font2 = {"family":"arial","color":"blue","size":10}


plt.plot(x,y)
plt.title("My plot",fontdict=font1,loc="left")
plt.xlabel("X coordinates ---->",fontdict=font2)
plt.ylabel("Y coordinates ---->",fontdict=font2)

plt.show()