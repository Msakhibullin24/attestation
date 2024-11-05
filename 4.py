import seaborn as sns
import scipy.stats as stats

df = sns.load_dataset('mpg').dropna()

# Разделение данных по типу двигателя
usa_mpg = df[df['origin'] == 'usa']['mpg']
euro_mpg = df[df['origin'] == 'euro']['mpg']
japan_mpg = df[df['origin'] == 'japan']['mpg']

# Проверка размера выборок
print(f'Размер выборки USA: {len(usa_mpg)}')
print(f'Размер выборки Euro: {len(euro_mpg)}')
print(f'Размер выборки Japan: {len(japan_mpg)}')

# выборки достаточно велики
if min(len(usa_mpg), len(euro_mpg), len(japan_mpg)) < 5:
    print("Одна или несколько выборок слишком малы для ANOVA. Используйте непараметрический тест (например, Kruskal-Wallis).")
else:
    # ANOVA
    anova = stats.f_oneway(usa_mpg, euro_mpg, japan_mpg)
    print(f'Гипотеза 2: ANOVA F={anova.statistic:.4f}, p={anova.pvalue:.4f}')
    print("Результат:", "Отвергаем H0" if anova.pvalue < 0.05 else "Не отвергаем H0")



''' 
вывод: 
        Первая гипотеза: Если p_corr < 0.05, это значит, что мощность двигателя  связан с расходом топлива.
        Вторая гипотеза: Если anova.pvalue < 0.05, существуют  различия в расходе топлива между автомобилями разного происхождения.

 Объяснение выбора критериев:
            Проверка гипотезы о корреляции:   анализируется связь между двумя числовыми переменными (мощность двигателя и расход топлива).

            ANOVA: анализ  для проверки различий среднего значения расхода топлива между группами (страны происхождения автомобилей)

'''
