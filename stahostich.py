# Стохастический градиентный спуск
theta_sgd = np.random.randn(2)
n_epochs = 50

for _ in range(n_epochs):
    for i in range(len(y)):
        rand_index = np.random.randint(len(y))
        xi = X_b[rand_index:rand_index + 1]
        yi = y[rand_index]
        gradients = 2 * xi.T.dot(xi.dot(theta_sgd) - yi)
        theta_sgd -= lr * gradients

print("Стохастический градиентный спуск:", theta_sgd)

# Визуализация
plt.scatter(X, y)
plt.plot(X, X_b.dot(theta_sgd), color='green')
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.title('Стохастический градиентный спуск')
plt.show()