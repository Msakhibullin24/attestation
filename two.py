import seaborn as sns
df = sns.load_dataset('mpg')
print(f'Количество строк: {df.shape[0]}, Количество столбцов: {df.shape[1]}')