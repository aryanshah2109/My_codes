import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print(sns.get_dataset_names())

crashes_df = sns.load_dataset('car_crashes')
print(crashes_df.to_string())

