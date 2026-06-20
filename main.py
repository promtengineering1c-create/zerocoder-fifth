import pandas as pd
# df = pd.read_csv('benchmark_scores.csv')

# print(df.info())
# print('----------------------------------     ----------------------------------')
# print(df.describe())
# print('----------------------------------     ----------------------------------')
# print(df.head())

df = pd.read_csv('dz.csv')

# print(df.info())

group = df.groupby('City')['Salary'].mean()

print(group)