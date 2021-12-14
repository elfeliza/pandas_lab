import pandas as pd

data = pd.read_csv('transactions.csv', delimiter=',')
print(data[data['STATUS']=='OK'].sort_values(by='SUM', ascending=False).head(3))
data1 = data[data['CONTRACTOR']=='Umbrella, Inc']
data2 = data1[data1['STATUS']=='OK']
Total = data2['SUM'].sum()
print(Total)
# rjvvurveruh
