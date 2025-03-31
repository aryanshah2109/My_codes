import matplotlib.pyplot as plt
import numpy as np
x = np.array([2,3,5,6,9])
y = np.array([1,5,6,9,10])

plt.plot(x,y)
plt.xlabel("X coordinates ---->")
plt.ylabel("Y coordinates ---->")
plt.title("My plot")
plt.show()