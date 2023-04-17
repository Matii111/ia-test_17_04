import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataset.csv',sep=';')

#replace strings to int values
data['estado'] = data['estado'].replace({'A': 1, 'R': 0})
#counts state values
counts = data['estado'].value_counts()
#select data
table1 = data.iloc[1:, :]

total = len(table1)

plt.bar(['0', '1', 'Total'],\
        [counts[0], counts[1], total],\
        edgecolor='black')
plt.xticks([0, 1, 2], ['0', '1', 'Total'])
plt.show()

# print(table1)
