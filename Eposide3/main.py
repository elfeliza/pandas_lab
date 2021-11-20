import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_html('r.html')
data1 = pd.read_excel('s.xlsx')
print(type(data))
all = data[0].merge(data1, left_on='User', right_on='login')
A = all.groupby('group_faculty')[['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']].mean()
B = all.groupby('group_out')[['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']].mean()
A.plot(kind='bar')
plt.xticks(rotation=0)
B.plot(kind='bar')
plt.xticks(rotation=0)
value = (all[(all['H'] >= 10) | (all['G'] >= 10)])
faculty = value['group_faculty'].unique()
groups = value['group_out'].unique()
print(faculty, groups)
plt.show()
