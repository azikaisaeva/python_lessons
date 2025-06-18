### Инкапсуляция в ООП (Объектно-Ориентированном Программировании)
from collections.abc import async_generator


# **Инкапсуляция** — это принцип ООП, который заключается в скрытии внутренней реализации объекта от внешнего мира и предоставлении доступа к данным и методам объекта только через специально определённые интерфейсы.
#
# Этот принцип позволяет:
#
# 1. Защитить данные от прямого изменения, обеспечив контроль над тем, как данные используются.
# 2. Сделать код более гибким и безопасным, так как изменения в одной части программы не повлияют на другие.
# 3. Спрятать детали реализации объекта, оставив только необходимые интерфейсы для работы с ним.
#
# ### Пример 1: Простая инкапсуляция с использованием геттеров и сеттеров
#
# В этом примере создадим класс `Person`, который инкапсулирует возраст человека, чтобы нельзя было установить отрицательное значение для возраста.

#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age  # Приватный атрибут

    # # Геттер для получения возраста
    # def get_age(self):
    #     return self.__age
    #
    # # Сеттер для установки возраста с проверкой
    # def set_age(self, age):
    #     if age < 0:
    #         print("Возраст не может быть отрицательным.")
    #     else:
    #         self.__age = age

# Создание объекта
# person = Person("John", 25)
#
# # Доступ к возрасту через методы
# print(person.get_age())  # 25
#
# # Попытка установить неправильный возраст
# person.set_age(-5)  # Возраст не может быть отрицательным.
# print(person.get_age())
# # Установка корректного возраста
# person.set_age(30)
# print(person.get_age())  # 30

# **Объяснение:**
#
# * Приватный атрибут `__age` не доступен напрямую извне класса.
# * Используем методы `get_age` и `set_age` для безопасного получения и изменения значения возраста. Метод `set_age` проверяет корректность значения перед установкой.

### Пример 2: Инкапсуляция с приватным методом

# В следующем примере создадим класс `BankAccount`, который инкапсулирует балансы и методы для их изменения.

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # Приватный атрибут

    # # Геттер для получения баланса
    # def get_balance(self):
    #     return self.__balance
    #
    # # Приватный метод для обновления баланса
    # def __update_balance(self, amount):
    #     self.__balance += amount

    # Метод для пополнения счета
    # def deposit(self, amount):
    #     if amount > 0:
    #         self.__update_balance(amount)
    #         print(f"Пополнено на {amount}")
    #     else:
    #         print("Сумма пополнения должна быть положительной.")

    # Метод для снятия средств
    # def withdraw(self, amount):
    #     if amount > 0 and amount <= self.__balance:
    #         self.__update_balance(-amount)
    #         print(f"Снято {amount}")
    #     else:
    #         print("Недостаточно средств или неверная сумма.")

# Создание объекта
# account = BankAccount("Alice", 1000)
#
# # Пополнение счета
# account.deposit(500)  # Пополнено на 500
#
# # Снятие средств
# account.withdraw(300)  # Снято 300
#
# # Получение текущего баланса
# print(account.get_balance())  # 1200

# **Объяснение:**
#
# * Приватный метод `__update_balance` обновляет баланс, но не доступен для прямого использования извне.
# * Метод `deposit` и `withdraw` предоставляют интерфейс для работы с балансом, а детали реализации скрыты.
# * Использование инкапсуляции позволяет избежать ошибок, связанных с прямым изменением баланса.

### Пример 3: Инкапсуляция с абстракцией

# Теперь создадим класс `Employee`, который инкапсулирует имя, возраст и зарплату, но скрывает детали, как рассчитывается зарплата.


# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.__salary = salary  # Приватный атрибут
#
#     # Геттер для зарплаты
#     def get_salary(self):
#         return self.__salary

    # # Сеттер для установки зарплаты
    # def set_salary(self, salary):
    #     if salary < 0:
    #         print("Зарплата не может быть отрицательной.")
    #     else:
    #         self.__salary = salary

    # Метод для увеличения зарплаты
    # def increase_salary(self, percentage):
    #     if percentage > 0:
    #         self.__salary += self.__salary * (percentage / 100)
    #         print(f"Зарплата увеличена на {percentage}%")
    #     else:
    #         print("Процент повышения должен быть положительным.")

# Создание объекта
# employee = Employee("Eve", 30, 5000)
#
# # Увеличение зарплаты
# employee.increase_salary(10)  # Зарплата увеличена на 10%
#
# # Получение зарплаты
# print(employee.get_salary())  # 5500
#
# # Установка новой зарплаты
# employee.set_salary(6000)
# print(employee.get_salary())  # 6000


# **Объяснение:**
#
# * Метод `increase_salary` скрывает детали, как именно вычисляется увеличение зарплаты, предоставляя абстракцию для пользователей.
# * Приватный атрибут `__salary` не может быть изменен напрямую извне, и любые изменения должны проходить через предоставленные методы.

### Резюме:

# Инкапсуляция — это принцип ООП, который скрывает внутреннюю реализацию класса и предоставляет интерфейс для работы с объектами. Это помогает обеспечить контроль над доступом к данным и улучшить безопасность программы.
#
# * Приватные атрибуты и методы скрыты от пользователя и доступны только через публичные интерфейсы (геттеры и сеттеры).
# * С помощью инкапсуляции можно скрыть сложную логику и оставить только необходимые для пользователя функции.



# Урок 28: Инкапсуляция - Задачи

# 1. Создайте класс Person, который имеет публичный атрибут name и приватный атрибут age.
# Реализуйте геттер и сеттер для age, чтобы нельзя было установить возраст менее 0.
# Используйте геттер для получения возраста и сеттер для изменения значения.
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if self.__age < 0:
#             print("Возраст не может быть отрицательным")
#         else:
#             self.__age = age
#
# person = Person("Steve", 34)
# print(person.get_age())
# person.set_age(30)
# print(person.get_age())


# 2. Создайте класс BankAccount, который имеет приватный атрибут balance.
# Реализуйте геттер и сеттер для баланса, чтобы нельзя было вывести больше денег, чем на счете.
#
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def __update_balance(self, amount):
#         self.__balance += amount
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__update_balance(amount)
#             print(f'Снято {amount}')
#         else:
#             print("Недостаточно средств на счету")
#
# account = BankAccount(2000)
# account.withdraw(400)
# account.withdraw(5000)

# 3. Создайте класс Book, который имеет публичный атрибут title и приватный атрибут author.
# Реализуйте методы для изменения имени автора через сеттер.

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.__author = author
#
#     def set_author(self, author):
#         return self.__author
#
# book = Book("Great Gatsby", "Scott Fitzgerald")
# book.set_author("Oscar Wilde")
# print(book)


# 4. Создайте класс Rectangle с приватными атрибутами length и width.
# Добавьте геттеры и сеттеры для изменения этих значений.
# Реализуйте метод для вычисления площади прямоугольника.

# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def set_length(self, value):
#         self.__length = value
#
#     def set_width(self, value):
#         self.__width = value
#
#     def calculate_rectangle_area(self):
#         return self.__length * self.__width
#
# area = Rectangle(5, 3)
# print(area.calculate_rectangle_area())


# 5. Создайте класс Product, который будет иметь приватные атрибуты name, price и quantity.
# Напишите методы для изменения этих атрибутов с проверками на правильность данных (например, цена не может быть отрицательной).
#
# class Product:
#     def __init__(self, name, price, quantity):
#         self.__name = name
#         self.__price = price
#         self.__quantity = quantity
#
#     def get

# 6. Создайте класс Circle, который имеет приватный атрибут radius.
# Напишите методы для получения и изменения радиуса круга и для вычисления его площади.
#
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#
#     def get_radius(self):
#         return self.__radius
#
#     def set_radius(self, value):
#         if value > 0:
#             self.__radius = value
#         else:
#             print("Радиус должен быть положительным")
#
#     def area(self):
#         return 3.14 * self.__radius ** 2
#
#
# circle = Circle(3)
# print(circle.get_radius())
# print(circle.area())


# 7. Создайте класс Student, который имеет публичный атрибут name и приватный атрибут marks.
# Реализуйте методы для добавления и получения оценок, с возможностью вывода среднего балла.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks
#
#     def get_marks(self):
#         return self.__marks
#
#     def set_marks(self, value):
#         self.__marks = value
#
#     def add_mark(self, mark):
#         self.__marks.append(mark)
#         return  self.__marks
#
#     def average(self):
#         return sum(self.__marks) / len(self.__marks)
#
# student = Student("Anna", [4])
# print(student.add_mark(3))
# print(student.average())


# 8. Добавьте в класс Employee метод display_salary(), который будет показывать зарплату сотрудника,
# если она больше 1000, иначе вывести сообщение "Зарплата недостаточна".
#
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#     def display_salary(self):
#         if self.__salary > 1000:
#             print(f"Зарплата сотрудника {self.name}: {self.__salary}")
#
#         else:
#             print("Зарплата недостаточна")
#
#
# employee1 = Employee("Anna", 1200)
# employee2 = Employee("Борис", 800)
# employee1.display_salary()
# employee2.display_salary()

# 9. Создайте класс Vehicle, который имеет приватные атрибуты make, model, и year.
# Напишите методы для получения и изменения этих атрибутов.
# Реализуйте метод для вычисления возраста автомобиля.
#
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.__make = make
#         self.__model = model
#         self.__year = year
#
#     def get_make(self):
#         return self.__make
#
#     def get_model(self):
#         return self.__model
#
#     def get_year(self):
#         return self.__year
#
#     def set_make(self, value):
#         self.__make = value
#
#     def set_model(self, value):
#         self.__model = value
#
#     def set_year(self, value):
#         self.__year = value
#
#     def car_age(self):
#         current_year = 2025
#         return current_year - self.__year
#
# v = Vehicle("Toyota", "Alphard",  2020)
# print(v.car_age())

# 10. Создайте класс Person, который имеет приватные атрибуты name и phone_number.
# Реализуйте метод для изменения номера телефона с проверкой на его корректность.
#
# class  Person:
#     def __init__(self, name, phone_number, new_number):
#         self.__name = name
#         self.__phone_number = phone_number
#
#     def get_name(self):
#         return self.__name
#
#     def get_number(self):
#         return self.__phone_number
#
#     def set_name(self, value):
#         self.__name = value
#
#     def set_number(self, new_number):
#         if new_number.isdigit():
#             self.__phone_number = new_number
#             print("Номер веден верно")
#         else:
#             print("Номер введен не правильно")
#
# p = Person("Alice", 2398649789)
# print(p.get_name())
# print(p.get_number())
# p.set_number("9867532879809")
# print("Новый номер: ", p.set_number())

# 11. Создайте класс Movie, который имеет приватные атрибуты title, director, и release_year.
# Реализуйте метод для вывода информации о фильме.
#
# class Movie:
#     def __init__(self, title, director, release_year):
#         self.__title = title
#         self.__director = director
#         self.__release_year = release_year
#
#     def get_movie(self):
#         print(f"Название фильма:", self.__title)
#         print(f"Режиссер: ", self.__director)
#         print(f"Дата выхода: ", self.__release_year)
#
# m = Movie("Eat. Pray. Love", "Ryan Murphy", 2019)
# print(m.get_movie())

# 12. Создайте класс Employee, который имеет публичный атрибут name и приватный атрибут salary.
# Напишите геттер и сеттер для зарплаты, с проверкой, что зарплата не может быть меньше 0.


# 13. Создайте класс Ticket, который имеет приватные атрибуты price, seat_number.
# Реализуйте методы для изменения цены билета и номера места с проверкой на корректность данных.

# 14. Создайте класс LibraryBook, который имеет публичные атрибуты title и приватные атрибуты author и publication_year.
# Напишите методы для получения информации о книге.

# 15. Создайте класс Account, который имеет приватные атрибуты account_number и balance.
# Реализуйте методы для пополнения счета и вывода средств с проверкой на достаточность средств.
