
# Урок 27: Введение в ООП (Объектно-Ориентированное Программирование)

# 1. Что такое ООП (Объектно-Ориентированное Программирование)?
# ООП — это методология программирования, основанная на концепции объектов и классов.
# Классы представляют собой шаблоны для создания объектов.
# Объекты — это экземпляры классов, которые содержат данные (атрибуты) и методы для работы с этими данными.

# Пример:
class Person:
    """Класс, описывающий человека."""
    def __init__(self, name, age):
        # конструктор: инициализирует атрибуты
        self.name = name      # атрибут экземпляра
        self.age = age
        # print("method init called!")

    def greet(self):
        # метод экземпляра
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")

# создание объекта
# p = Person("Алиса", 30)

# p.greet()  # Привет, меня зовут Алиса, мне 30 лет.


# 2. Основные элементы ООП:
# Классы и объекты:
# Класс — это как шаблон для объектов.
# Объект — это экземпляр класса.

# Пример:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# animal1 = Animal("Dog")
# print(animal1.speak())  # Output: Dog makes a sound.


# Конструктор __init__():
# Метод __init__ используется для инициализации объекта с атрибутами, которые он будет содержать.

# Пример:

class Car:
    def __init__(self, make, model, wheels=4):
        self.wheels = wheels
        self.make = make
        self.model = model
#
# my_car = Car("Toyota", "Corolla")
# print(my_car.make, my_car.model, my_car.wheels)  # Output: Toyota Corolla


# 3. Методы и атрибуты:
# Атрибуты — это переменные, которые хранят информацию о объекте.
# Методы — это функции, которые выполняют операции с атрибутами объекта.

# Пример:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} barks!"

# dog1 = Dog("Buddy", "Golden Retriever")
# print(dog1.bark())  # Output: Buddy barks!


# 4. Подведение итогов:
# ООП является мощной концепцией, которая позволяет создавать гибкие и масштабируемые программы.
# В ООП важны классы и объекты как основные элементы. 
# В следующем уроке мы подробно рассмотрим инкапсуляцию, полиморфизм, наследование и абстракцию в ООП.

# Домашнее задание (Задачи для практики):
# 1. Создайте класс Car, который имеет атрибуты make (марка автомобиля), model (модель) и year (год выпуска).
# Добавьте метод get_car_info(), который выводит информацию о машине.


# 2. Создайте класс Circle, который имеет атрибут radius (радиус).
# Добавьте методы для вычисления площади и периметра круга.


# 3. Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота).
# Добавьте метод для вычисления площади прямоугольника.

# 4. Реализуйте полиморфизм, создав классы Bird и Fish, которые переопределяют метод move(),
# в котором будет описан способ передвижения (полет и плавание соответственно).

# 5. Создайте класс Person с атрибутами name и age. Реализуйте метод greet(), который будет возвращать приветствие.


# ДЗ


# 1. **Класс «Круг»**
#    Создайте класс `Circle` с публичным атрибутом `radius` (радиус). Добавьте метод `area()`, возвращающий площадь круга (`π * radius**2`), и метод `circumference()`, возвращающий длину окружности (`2 * π * radius`).
#
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius

# radius1 = Circle(6)
# print(radius1.area())
# print(radius1.circumference())


# 2. **Класс «Студент»**
#    Определите класс `Student` с атрибутами `name` (имя) и `grades` (список оценок). Реализуйте методы:
#    * `add_grade(grade)` — добавить оценку в список;
#    * `average()` — вычислить и вернуть среднее арифметическое всех оценок.
#
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         return self.grades.append(grade)
#
#     def average(self):
#         return sum(self.grades) / len(self.grades)
#
# s = Student("Kamila")
# s.add_grade(4)
# s.add_grade(5)
# print(s.average())



# 3. **Класс «Вектор 2D»**
#    Напишите класс `Vector2D` с атрибутами `x` и `y`. Реализуйте «магические» методы:
#
#    * `__add__(other)` для сложения двух векторов;
#    * `__sub__(other)` для вычитания;
#    * `__repr__()` для удобного строкового представления.

# class Vektor2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self):
#         return self.x + self.y
#
#     def __sub__(self):
#         return self.x - self.y
#
#     def __repr__(self):
#         return f"Vector2D({self.x}, {self.y})"
#
# v = Vektor2D(1,2)
# print(v)
#
# 4. **Класс «Книга»**
#    Создайте класс `Book` с атрибутами `title`, `author` и `pages` (кол-во страниц). Добавьте метод `description()`, возвращающий строку:
#
#    ```
#    "<title> — автор <author>, <pages> стр."
#    ```
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def description(self):
#         return f"{self.title} - автор {self.author}, {self.pages} стр. "
#
# b = Book("The Great Gatsby", "F. Scott Fitzgerald", 78)
# print(b.description())

# 5. **Класс «Точка»**
#    Определите класс `Point` с координатами `x` и `y`. Добавьте метод `distance_to_origin()`, возвращающий расстояние от точки до начала координат, и метод `distance_to(other)`, возвращающий расстояние до другой точки.

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def distance_to_origin(self):

# 6. **Класс «Конвертер температур»**
#    Напишите класс `TemperatureConverter` с двумя статическими методами (без использования `@classmethod`):
#
#    * `c_to_f(celsius)` — перевод из °C в °F;
#    * `f_to_c(fahrenheit)` — перевод из °F в °C.
#
# class TemperatureConverter:
#     def __init__(self, celsius, fahrenheit):
#         self.celsius = celsius
#         self.fahrenheit = fahrenheit
#
#     def c_to_f(self, celsius):
#         return celsius * 9 / 5 + 32
#
#     def f_to_c(self, fahrenheit):
#         return (fahrenheit - 32) * 5 / 9
# #
# converter = TemperatureConverter(32, 212)
# print(converter.c_to_f)
# print(converter.f_to_c)
# #
# 7. **Класс «Матрица 2×2»**
#    Создайте класс `Matrix2x2`, хранящий четыре числа `a, b, c, d`. Реализуйте методы:
#
#    * `determinant()` — вычисление определителя;
#    * `__mul__(other)` — умножение двух матриц 2×2.

# class Matrix22:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d

#     def determinant(self):
#         return self.a * self.d - self.b * self.c
#
#     def __mul__(self, other):
#         a = self.a * other.a + self.b * other.c
#         b = self.a * other.b + self.b * other.d
#         c = self.c * other.a + self.d * other.c
#         d = self.c * other.b + self.d * other.d
#         return Matrix22(a, b, c, d)
#
# m1 = Matrix22(1, 2, 3, 4)
# m2 = Matrix22(5, 6, 7, 8)
# print(m1)
# print(m2)
#
# 8. **Класс «Список покупок»**
#    Определите класс `ShoppingList` с атрибутом `items` (список строк). Реализуйте методы:
#
#    * `add(item)` — добавить товар;
#    * `remove(item)` — удалить товар по имени (если есть);
#    * `show()` — вывести все товары в виде нумерованного списка.

# class Shoppinglist:
#     def __init__(self, items):
#         self.items = []
#
#     def __add__(self, item):
#         self.items.append(item)
#         print(f"Товар {item} добавлен в список")
#
#     def remove(self, item):
#         if item in self.items:
#             self.items.remove(item)
#             print(f"Товар {item} удален из списка")
#
#     def show(self):
#         for i in range(len(self.items)):
#             print(f"{i + 1}. {self.items[i]}")
#
# my_list = Shoppinglist(items= "Молоко")
# print(my_list)
# my_list.__add__("Хлеб")
# my_list.show()
# my_list.remove("Молоко")

#
# 9. **Класс «Комплексное число»**
#    Напишите класс `ComplexNumber` с атрибутами `real` и `imag`. Реализуйте методы:
#
#    * `__add__(other)` и `__mul__(other)` для сложения и умножения комплексных чисел;
#    * `__repr__()` для отображения в формате `"a + bi"` или `"a - bi"`.

# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __add__(self, other):
#         new_real = self.real + other.real
#         new_imag = self.imag + other.imag
#         return ComplexNumber(new_real, new_imag)
#
#     def __mul__(self, other):
#         new_real = self.real * other.real - self.imag * other.imag
#         new_imag = self.real * other.imag + self.imag * other.real
#         return ComplexNumber(new_real, new_imag)
#
#     def __repr__(self):
#         return f'ComplexNumber{self.real}, {self.imag}'
#
# z1 = ComplexNumber(3, 4)
# z2 = ComplexNumber(6, 7)
# print(z1 + z2)
# print(z1 * z2)
# #
# 10. **Класс «Счётчик»**
#     Создайте класс `Counter` с атрибутом `value`, инициализируемым в конструкторе. Добавьте методы:
#
#     * `increment()` — увеличить на 1;
#     * `decrement()` — уменьшить на 1;
#     * `reset()` — обнулить;
#     * `__repr__()` — вернуть текущее значение в виде строки.

# class Counter:
#     def __init__(self, value):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#         return self.value
#
#     def decrement(self):
#         self.value -= 1
#         return self.value
#
#     def reset(self):
#         self.value = 0
#         return self.value
#
#     def __repr__(self):
#         return str(self.value)
#
# c = Counter(10)
# c.increment()
# print(c)
# c.decrement()
# print(c)
# c.reset()
#
