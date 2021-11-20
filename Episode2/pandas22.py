import pandas as pd
import pylab
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

data = pd.read_csv('f.csv', delimiter=',')
company = data['CARGO'].value_counts()
pr_we = data.groupby('CARGO')[['PRICE', 'WEIGHT']].sum()
plt.bar(company.index, company, color=['purple', 'pink', 'magenta'])
plt.xlim([-0.5, 3])
Nimble = mpatches.Patch(color='purple',
                        label=str(pr_we.iloc[0]['WEIGHT']) + ' kg' + ', ' + str(pr_we.iloc[0]['PRICE']) + ' rub')
Medium = mpatches.Patch(color='pink',
                        label=str(pr_we.iloc[1]['WEIGHT']) + ' kg' + ', ' + str(pr_we.iloc[1]['PRICE']) + ' rub')
Jumbo = mpatches.Patch(color='magenta',
                       label=str(pr_we.iloc[2]['WEIGHT']) + ' kg' + ', ' + str(pr_we.iloc[2]['PRICE']) + ' rub')
plt.legend(handles=[Nimble, Medium, Jumbo])
plt.title('ALL THE DATA')
plt.show()
