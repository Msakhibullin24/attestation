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

#еще можно решить сразу все вместе:
'''
import seaborn as sns
import pandas as pd

df = sns.load_dataset('mpg')
# Создаем пустой словарь для хранения результатов
numeric_summary = {}

for col in df.select_dtypes(include=['number']).columns:
    numeric_summary[col] = {
        'Доля пропусков': df[col].isnull().mean(),
        'Максимальное значение': df[col].max(),
        'Минимальное значение': df[col].min(),
        'Среднее значение': df[col].mean(),
        'Медиана': df[col].median(),
        'Дисперсия': df[col].var(),
        'Квантиль 0.1': df[col].quantile(0.1),
        'Квантиль 0.9': df[col].quantile(0.9),
        'Квартиль 1': df[col].quantile(0.25),
        'Квартиль 3': df[col].quantile(0.75)
    }

numeric_summary_df = pd.DataFrame(numeric_summary).T

print("Числовой анализ:")
print(numeric_summary_df)

'''
