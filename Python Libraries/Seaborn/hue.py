import seaborn as sns
import matplotlib.pyplot as plt

d = sns.load_dataset('penguins')
print(d.keys())
# print(d.to_string())
# sns.lineplot(x='passengers',y='fare',data=dataTaxis)
# plt.show()


sns.lineplot(x='bill_length_mm',y='bill_depth_mm',data=d,hue='sex')
plt.show()

