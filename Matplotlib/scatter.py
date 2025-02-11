import matplotlib.pyplot as plt
import numpy as np
# doesnt have lines but just coordinates
# useful for comparison of 2 or more graphs

x = np.array([1,2,3,5,4,2,6,1,8,10])
y = np.array([1,5,4,7,2,3,2,9,1,11])

plt.scatter(x,y)

x = np.array([4,3,6,3,9,1,6,9,10,14])
y = np.array([6,1,7,9,1,4,11,13,15,9])

plt.scatter(x,y)

plt.show()
