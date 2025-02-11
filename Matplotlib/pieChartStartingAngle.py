import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,5,2,7])
myLabels = ["A","B","C","D"]
plt.pie(x,labels=myLabels,startangle=90)
plt.show()