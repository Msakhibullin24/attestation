import seaborn as sns
import numpy as np
import pandas as pd
import scipy.stats as stats

# 1. Загрузка данных
df = sns.load_dataset('mpg').dropna()

# Гипотеза 1: Влияние мощности двигателя на расход топлива
# Нулевая гипотеза (H0): horsepower не влияет на mpg
# Альтернативная гипотеза (H1): horsepower влияет на mpg

# 2. Корреляционный анализ
correlation, p_value_correlation = stats.pearsonr(df['horsepower'], df['mpg'])

# Вывод результатов корреляционного анализа
print(f'Гипотеза 1: Корреляционный анализ')
print(f'Коэффициент корреляции: {correlation:.4f}, p-значение: {p_value_correlation:.4f}')
if p_value_correlation < 0.05:
    print("Отвергаем H0: существует значимая связь между horsepower и mpg.")
else:
    print("Не можем отвергнуть H0: связь между horsepower и mpg незначима.")
print('')

# Гипотеза 2: Различия в расходе топлива между типами двигателей
# Нулевая гипотеза (H0): Средний расход топлива (mpg) одинаков для всех типов
# Альтернативная гипотеза (H1): Средний расход топлива (mpg) различается между типами

# 3. ANOVA
# Разделение данных по типу двигателя
usa_mpg = df[df['origin'] == 'usa']['mpg']
euro_mpg = df[df['origin'] == 'euro']['mpg']
japan_mpg = df[df['origin'] == 'japan']['mpg']

anova_result = stats.f_oneway(usa_mpg, euro_mpg, japan_mpg)

# Вывод результатов ANOVA
print(f'Гипотеза 2: ANOVA')
print(f'F-статистика: {anova_result.statistic:.4f}, p-значение: {anova_result.pvalue:.4f}')
if anova_result.pvalue < 0.05:
    print("Отвергаем H0: существуют значимые различия в расходе топлива между типами двигателей.")
else:
    print("Не можем отвергнуть H0: расход топлива одинаков для всех типов двигателей.")
