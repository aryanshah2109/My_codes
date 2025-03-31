import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([1,5,2,7])

plt.bar(x,y,color="r",width=0.2)    
# plt.barh(x,y,color="r") returns horizontal bars
# for horizontal bars, we use height= instead of width
plt.show()