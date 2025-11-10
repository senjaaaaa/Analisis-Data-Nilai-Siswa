import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilaisiswa.csv')

print(data.head())

data.info()
data.head()
data.describe()

print("Rata-rata : ", data['Nilai'].mean())
print("Median : ", data['Nilai'].median())
print("Modus : ", data['Nilai'].mode()[0])

matematika = data[data['Matpel'] == 'Matematika']

print(matematika)

data.groupby('Matpel')['Nilai'].agg(['max','min'])

rata = data.groupby('Matpel')['Nilai'].mean()

rata.plot(kind='bar')

plt.title('Rata-rata Nilai per-mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-rata')
plt.show()

sns.boxplot(x='Mapel', y='Nilai', data=data)

plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()