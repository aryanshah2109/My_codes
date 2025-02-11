import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([10,23,45,50,90])
plt.plot(x,y)
plt.grid()
plt.show()

# we can even just give one axis for single grid lines
# by plt.grid(axis="x")