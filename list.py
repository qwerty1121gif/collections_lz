def fibonacci_sequence(n):
  """Генерирует ряд Фибоначчи до n-го числа."""
  sequence = [0, 1]
  if n <= 2:
    return sequence[:n]
  for i in range(2, n):
    next_number = sequence[-1] + sequence[-2]
    sequence.append(next_number)
  return sequence

def main():
  n = int(input("Введите N: "))

  fib_sequence = fibonacci_sequence(n)

  # Модифицируем список
  for i in range(len(fib_sequence)):
    if fib_sequence[i] % 2 == 0:
      fib_sequence[i] *= 2
    else:
      fib_sequence[i] **= 2

  # Находим минимальный и максимальный элементы
  min_value = min(fib_sequence)
  max_value = max(fib_sequence)

  # Находим длину и количество элементов
  length = len(fib_sequence)
  count = len(fib_sequence)

  # Находим медианное значение
  median_value = fib_sequence[length // 2] if length % 2 != 0 else (fib_sequence[length // 2 - 1] + fib_sequence[length // 2]) / 2

  # Считаем количество элементов, большее медианного
  count_greater_median = sum(1 for x in fib_sequence if x > median_value)

  print(f"Список Фибоначчи до {n} элементов: {fib_sequence}")
  print(f"Минимальный элемент: {min_value}")
  print(f"Максимальный элемент: {max_value}")
  print(f"Длина списка: {length}")
  print(f"Количество элементов: {count}")
  print(f"Медианное значение: {median_value}")
  print(f"Количество элементов больше медианы: {count_greater_median}")

if __name__ == "__main__":
  main()

