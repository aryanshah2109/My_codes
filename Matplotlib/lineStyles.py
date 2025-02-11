import matplotlib.pyplot as plt
import numpy as np
x = np.array([2,3,5,6,9])
y = np.array([1,5,6,9,10])

# color = color of lines
# linewidth = width of lines
# linestyle = type of line
plt.plot(x,y,color = "red", linewidth=10, linestyle = "dashed")
plt.show()