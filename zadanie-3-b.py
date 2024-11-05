import seaborn as sns
import pandas as pd

df = sns.load_dataset('mpg')

categorical_cols = df.select_dtypes(include=['object', 'category']).columns
print(df[categorical_cols].describe().T)  # Показывает count, unique, top, freq для каждой категориальной переменной


# Анализ категориальных переменных


'''

# или же можно было бы решить так  если более подробно и четко расспсиывать 
import pandas as pd

# Создание DataFrame вручную
data = {
    'Числовой_столбец1': [1, 2, 3, None, 5],
    'Числовой_столбец2': [10, 15, None, 20, 25],
    'Категориальный_столбец1': ['A', 'B', 'A', None, 'C']
}

df = pd.DataFrame(data)

for col in df.select_dtypes(include='object').columns:
    print(f'Категориальный столбец: {col}')
    print(f'Доля пропусков: {df[col].isnull().mean():.2%}')
    print(f'Количество уникальных значений: {df[col].nunique()}')
    print(f'Мода: {df[col].mode().iloc[0] if not df[col].mode().empty else "Нет моды"}')
    print('-' * 30)

'''
