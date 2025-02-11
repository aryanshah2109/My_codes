import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,5,2,7])
myLabels = ["A","B","C","D"]
myColors = ["red","green","black","magenta"]
plt.pie(x,labels=myLabels,colors=myColors)
plt.legend(title="My Legend")    # shows which color represents which portion
plt.show()