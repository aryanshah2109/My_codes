import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

crashes_df = sns.load_dataset('car_crashes')
sns.jointplot(x='alcohol',y='not_distracted',data=crashes_df, kind='hex')
plt.show()


