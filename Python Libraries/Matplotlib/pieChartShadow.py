import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,5,2,7])
myLabels = ["A","B","C","D"]
myExplode = [0,0.2,0,0] 
plt.pie(x,labels=myLabels,shadow=True,explode=myExplode)
plt.show()