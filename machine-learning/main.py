import pandas as pd
import numpy as np
import seaborn as sns
sns.set_palette('husl')

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
col_name = ['sepal-length','sepal-width','petal-length','petal-width','class']
data = pd.read_csv(url, names=col_name)

# print all data in columns
print(data)

# print details of data
print(data.shape)

# print first 5 columns
print(data.head())

data['class'].value_counts()
