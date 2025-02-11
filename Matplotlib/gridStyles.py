import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5])
y = np.array([10,23,45,50,90])
plt.plot(x,y)
plt.grid(color="red",linestyle="dotted",linewidth="1.5")
plt.show()