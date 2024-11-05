import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Сгенерируем данные (если что заменим этот шаг на загрузку данных из файла)
np.random.seed(42)
n_samples = 100
horsepower = np.random.uniform(50, 200, n_samples)
weight = np.random.uniform(1500, 4000, n_samples)
mpg = 50 - 0.01 * horsepower - 0.005 * weight + np.random.normal(0, 2, n_samples)

# Приведем данные в формат DataFrame
data = pd.DataFrame({
    'mpg': mpg,
    'horsepower': horsepower,
    'weight': weight
})

# Нормализуем данные для стабильности обучения
x = data['horsepower']
y = data['mpg']
x_normalized = (x - np.mean(x)) / np.std(x)
y_normalized = (y - np.mean(y)) / np.std(y)

# Реализация обычного градиентного спуска
def gradient_descent(x, y, lr=0.001, epochs=1000):
    m = 0  # начальный коэффициент
    b = 0  # начальное смещение
    n = len(y)
    for _ in range(epochs):
        y_pred = m * x + b
        d_m = (-2/n) * sum(x * (y - y_pred))
        d_b = (-2/n) * sum(y - y_pred)
        m -= lr * d_m
        b -= lr * d_b
    return m, b

# Реализация стохастического градиентного спуска
def stochastic_gradient_descent(x, y, lr=0.001, epochs=100):
    m = 0  # начальный коэффициент
    b = 0  # начальное смещение
    n = len(y)
    for _ in range(epochs):
        for i in range(n):
            xi = x.iloc[i]
            yi = y.iloc[i]
            y_pred = m * xi + b
            d_m = -2 * xi * (yi - y_pred)
            d_b = -2 * (yi - y_pred)
            m -= lr * d_m
            b -= lr * d_b
    return m, b

# Применяем обычный и стохастический градиентный спуск
m_gd, b_gd = gradient_descent(x_normalized, y_normalized, lr=0.001)
m_sgd, b_sgd = stochastic_gradient_descent(x_normalized, y_normalized, lr=0.001)

# Вывод результатов
print("Обычный градиентный спуск:")
print(f"m = {m_gd}, b = {b_gd}")
print("Стохастический градиентный спуск:")
print(f"m = {m_sgd}, b = {b_sgd}")
