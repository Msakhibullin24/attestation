import seaborn as sns
import pandas as pd

# Загрузка данных
df = sns.load_dataset('mpg')

# Количество строк и столбцов
print(f'Количество строк: {df.shape[0]}, Количество столбцов: {df.shape[1]}')
