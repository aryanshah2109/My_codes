import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

crashes_df = sns.load_dataset('car_crashes')
kde = sns.kdeplot(crashes_df['alcohol'])

plt.show()