
# Урок 27: Введение в ООП (Объектно-Ориентированное Программирование)

# 1. Что такое ООП (Объектно-Ориентированное Программирование)?
# ООП — это методология программирования, основанная на концепции объектов и классов.
# Классы представляют собой шаблоны для создания объектов.
# Объекты — это экземпляры классов, которые содержат данные (атрибуты) и методы для работы с этими данными.

# Пример:

class Person:
    """Класс, описывающий человека."""
    def __init__(self, name, age):
        #Дандр метод во внутренней библиотеке отвечает за инициализацию переменных на протяжении всего класса
        #конструктор: инициализирует атрибуты
        self.name = name    #Атрибуты класса
        self.age = age

    def greet(self):
        #метод экземпляра
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("John", 30)
print(person1.greet())  # Output: Hello, my name is John and I am 30 years old.


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

animal1 = Animal("Dog")
print(animal1.speak())  # Output: Dog makes a sound.


# Конструктор __init__():
# Метод __init__ используется для инициализации объекта с атрибутами, которые он будет содержать.

# Пример:

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.make, my_car.model)  # Output: Toyota Corolla


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

dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())  # Output: Buddy barks!


# 4. Подведение итогов:
# ООП является мощной концепцией, которая позволяет создавать гибкие и масштабируемые программы.
# В ООП важны классы и объекты как основные элементы. 
# В следующем уроке мы подробно рассмотрим инкапсуляцию, полиморфизм, наследование и абстракцию в ООП.

# Домашнее задание (Задачи для практики):
# 1. Создайте класс Car, который имеет атрибуты make (марка автомобиля), model (модель) и year (год выпуска).
# Добавьте метод get_car_info(), который выводит информацию о машине.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_car_info(self):
        return f"Car Info: {self.year} {self.make} {self.model}"

car = Car("Toyota", "Camry", 2022)
print(car.get_car_info())  # Output: Car Info: 2022 Toyota Camry


# 2. Создайте класс Circle, который имеет атрибут radius (радиус).
# Добавьте методы для вычисления площади и периметра круга.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print(circle.area())  # Output: 78.53981633974483
print(circle.perimeter())  # Output: 31.41592653589793


# 3. Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота).
# Добавьте метод для вычисления площади прямоугольника.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(10, 5)
print(rectangle.area())  # Output: 50


# 4. Реализуйте полиморфизм, создав классы Bird и Fish, которые переопределяют метод move(),
# в котором будет описан способ передвижения (полет и плавание соответственно).

class Bird:
    def move(self):
        return "I fly in the sky!"

class Fish:
    def move(self):
        return "I swim in the water!"

bird = Bird()
fish = Fish()
print(bird.move())  # Output: I fly in the sky!
print(fish.move())  # Output: I swim in the water!


# 5. Создайте класс Person с атрибутами name и age. Реализуйте метод greet(), который будет возвращать приветствие.
# Используя наследование, создайте класс Student, который будет добавлять атрибут student_id и переопределит метод greet().

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}."

student = Student("Alice", 20, "S1234")
print(student.greet())  # Output: Hello, my name is Alice, I am 20 years old, and my student ID is S1234.
