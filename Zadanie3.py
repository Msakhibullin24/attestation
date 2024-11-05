# Быстрый анализ числовых переменных
#print(df.describe().T)  # Показывает max для каждой числовой переменной



# а так можно решить вот так 
import pandas as pd

# Загрузите ваши данные
df = pd.read_csv('ваш_файл.csv')

# Проведение анализа
for column in df.select_dtypes(include='number').columns:
    print(f'Анализ для столбца: {column}')
    print(f'Доля пропусков: {df[column].isnull().mean():.2%}')
    print(f'Минимум: {df[column].min()}')
    print(f'Максимум: {df[column].max()}')
    print(f'Среднее: {df[column].mean()}')
    print(f'Медиана: {df[column].median()}')
    print(f'Дисперсия: {df[column].var()}')
    print(f'Квантиль 0.1: {df[column].quantile(0.1)}')
    print(f'Квантиль 0.9: {df[column].quantile(0.9)}')
    print(f'1-й квартиль: {df[column].quantile(0.25)}')
    print(f'3-й квартиль: {df[column].quantile(0.75)}')
    print('-' * 30)
