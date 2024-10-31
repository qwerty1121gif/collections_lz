import matplotlib.pyplot as plt
import numpy as np

# Определяем функцию
def func(x):
    return np.tan(5*x)**2 / np.cos(x**2)

# Генерируем 20 точек для графика
x = np.linspace(-1, 1, 20)

# Вычисляем значения функции для каждой точки
y = func(x)

# Рисуем график
plt.plot(x, y)

# Добавляем подписи к осям
plt.xlabel("x")
plt.ylabel("y")

# Добавляем заголовок графика
plt.title("График функции y = tg²(5x)/cos(x²)")

# Отображаем график
plt.show()

