import seaborn as sns
import pandas as pd

# Загрузка данных
df = sns.load_dataset('mpg')

# Количество строк и столбцов
print(f'Количество строк: {df.shape[0]}, Количество столбцов: {df.shape[1]}')



print(df.describe().T)  # Показывает max для каждой числовой переменной


# Быстрый анализ числовых переменных
'''

# а так можно решить с рассписанным максимально подрбно все тем что тут есть
import seaborn as sns
import pandas as pd

# Загрузка данных
df = sns.load_dataset('mpg')

# Количество строк и столбцов
print(f'Количество строк: {df.shape[0]}, Количество столбцов: {df.shape[1]}')
numeric_cols = df.select_dtypes(include=['number']).columns

eda_results = {}
for col in numeric_cols:
    eda_results[col] = {
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

# Преобразуем результаты в DataFrame для удобного отображения
eda_df = pd.DataFrame(eda_results).T

print(eda_df)

'''
