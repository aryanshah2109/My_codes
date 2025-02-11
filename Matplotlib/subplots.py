import matplotlib.pyplot as plt
import numpy as np

# first argument gives no of rows
# second argument gives no of cols
# third argument gives the no of plot

# max index = rows*cols

x = np.array([1,4,8,2])
y = np.array([10,20,50,30])

plt.subplot(2,2,1)
plt.plot(x,y)

x = np.array([1,2,3,2])
y = np.array([5,20,25,39])

plt.subplot(2,2,2)
plt.plot(x,y)

x = np.array([10,14,23,21])
y = np.array([10,20,50,30])

plt.subplot(2,2,3)
plt.plot(x,y)

x = np.array([1,5,3,7])
y = np.array([15,20,25,39])

plt.subplot(2,2,4)
plt.plot(x,y)

plt.show()