#Сначала градиентный спуск:
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Загружаем данные
df = sns.load_dataset('mpg').dropna()
X = df['horsepower'].values
y = df['mpg'].values
X_b = np.c_[np.ones(X.shape[0]), X]  # Добавляем единицы

# Параметры
lr = 0.01
n_iter = 1000
theta = np.random.randn(2)

# Обычный градиентный спуск
for _ in range(n_iter):
    gradients = 2 / len(y) * X_b.T.dot(X_b.dot(theta) - y)
    theta -= lr * gradients

print("Обычный градиентный спуск:", theta)

# Визуализация
plt.scatter(X, y)
plt.plot(X, X_b.dot(theta), color='red')
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.title('Обычный градиентный спуск')
plt.show()
