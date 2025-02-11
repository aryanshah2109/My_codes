import matplotlib.pyplot as plt
import numpy as np

# format string - fmt - marker|line|color

# color reference
# r red
# g green
# b blue
# c cyan
# k black
# m magenta
# y yellow
# w white


# line reference
# : is dotted lines
# - is normal line 
# -- is dashed line
# -. is dashed-dotted lines

x = np.array([3,5,7,8,9])
y = np.array([1,4,5,2,9])

plt.plot(x,y, "o--m")
plt.show()

