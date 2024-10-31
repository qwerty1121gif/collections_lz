import numpy as np

# Создаем единичную матрицу 5x5
matrix_fib = np.identity(5)

# Вычисляем первые 25 чисел Фибоначчи
fibonacci = [0, 1]
for i in range(2, 25):
  fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

# Складываем элементы матрицы с числами Фибоначчи
for i in range(5):
  for j in range(5):
    matrix_fib[i][j] += fibonacci[i*5 + j]

# Создаем единичную матрицу 5x5
matrix_bernoulli = np.identity(5)

# Вычисляем первые 25 чисел Бернулли (используя библиотеку sympy)
from sympy.ntheory.bernoulli import bernoulli
bernoulli_numbers = [bernoulli(i) for i in range(25)]

# Складываем элементы матрицы с числами Бернулли
for i in range(5):
  for j in range(5):
    matrix_bernoulli[i][j] += bernoulli_numbers[i*5 + j]

# Умножаем матрицы
result_matrix = np.dot(matrix_fib, matrix_bernoulli)

# Создаем матрицу для сравнения
compare_matrix = np.array([
  [10, 72, 80, 62, 34],
  [37, 10, 55, 90, 26],
  [45, 41, 15, 14, 44],
  [15, 8, 1, 23, 28],
  [67, 39, 89, 4, 23]
])

# Сравниваем матрицы
if np.sum(result_matrix) > np.sum(compare_matrix):
  print("Полученная матрица больше.")
else:
  print("Матрица для сравнения больше.")

# Выводим полученные матрицы
print("\nМатрица Фибоначчи:")
print(matrix_fib)
print("\nМатрица Бернулли:")
print(matrix_bernoulli)
print("\nРезультирующая матрица:")
print(result_matrix)
print("\nМатрица для сравнения:")
print(compare_matrix)
