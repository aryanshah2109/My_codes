import matplotlib.pyplot as plt
import numpy as np

x = np.array([3,5,7,8,9])
y = np.array([1,4,5,2,9])

# marker argument is used to emphasize each point specifically
# generally marker = "o"
# we can also take marker = "*"
plt.plot(x,y, marker="o")
plt.show()