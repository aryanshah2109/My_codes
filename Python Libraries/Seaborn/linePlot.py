import seaborn as sns
import matplotlib.pyplot as plt

dataTaxis = sns.load_dataset('taxis')
print(dataTaxis.keys())

sns.lineplot(x='passengers',y='fare',data=dataTaxis)
plt.show()




