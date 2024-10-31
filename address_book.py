address_book = {}

def add_entry():
 """Добавляет новую запись в адресную книгу."""
 name = input("Введите имя: ")
 address = input("Введите адрес: ")
 address_book[name] = address
 print(f"Запись для {name} добавлена.")

def change_address():
 """Изменяет адрес в адресной книге."""
 name = input("Введите имя, для которого нужно изменить адрес: ")
 if name in address_book:
  new_address = input(f"Введите новый адрес для {name}: ")
  address_book[name] = new_address
  print(f"Адрес {name} изменен на: {new_address}")
 else:
  print(f"Имя {name} не найдено в адресной книге.")

def delete_entry():
 """Удаляет запись из адресной книги."""
 name = input("Введите имя, запись которого нужно удалить: ")
 if name in address_book:
  del address_book[name]
  print(f"Запись для {name} удалена.")
 else:
  print(f"Имя {name} не найдено в адресной книге.")

def show_address_book():
 """Выводит весь словарь адресной книги."""
 if address_book:
  print("\nАдресная книга:")
  for name, address in address_book.items():
   print(f"{name}: {address}")
 else:
  print("Адресная книга пуста.")

while True:
 print("\nВыберите действие:")
 print("1. Добавить запись")
 print("2. Изменить адрес")
 print("3. Удалить запись")
 print("4. Показать адресную книгу")
 print("5. Выход")

 choice = input("Введите номер действия: ")

 if choice == '1':
  add_entry()
 elif choice == '2':
  change_address()
 elif choice == '3':
  delete_entry()
 elif choice == '4':
  show_address_book()
 elif choice == '5':
  print("До свидания!")
  break
 else:
  print("Неверный выбор действия.")
