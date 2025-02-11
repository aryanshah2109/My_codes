import matplotlib.pyplot as plt
import numpy as np
x = np.array([2,3,5,6,9])
y = np.array([1,5,6,9,10])

# ms -> marker size
# mec -> marker edge color = marker border color
# we can also use hash values of the colors or the name of the colors
# mfc -> marker face color = marker inside color

plt.plot(x,y,marker="o", ms = 10, mec = "r",mfc = "g")
plt.show()