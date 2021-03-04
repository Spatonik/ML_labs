import pandas
import matplotlib.pyplot as plt


file = pandas.read_csv('API.csv', skiprows=4, usecols=range(63))
file = file.rename(file.loc[file.index]['Country Name'])
file = file.drop(file.columns[:4], 1)
file.dropna(axis='columns', how='all', inplace=True)
file.dropna(axis='index', thresh=len(file.columns), inplace=True)

a = file.mean(axis='rows', numeric_only=True)
a.plot(grid=True, style='y.-', marker='o', title='Доступ к электричеству стран').get_figure().show()
plt.xlabel("year")
plt.ylabel("percent (%)")
plt.show()

b = file.loc[file.sum(axis='columns').sort_values(ascending=False)[:5].index].transpose()
b.plot(grid=True, style='.-', marker='o', title='Доступ к электричеству топ 5 стран с 1990 по 2018 (% - процент)')
plt.xlabel("year")
plt.ylabel("percent (%)")
plt.show()
