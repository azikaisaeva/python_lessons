"""
Урок 11: Циклы for и while, основные конструкции
"""

# Цикл for
"""
Цикл for используется для перебора элементов последовательности (списка, строки, кортежа, множества или диапазона чисел).
Синтаксис:

for переменная in последовательность:
    # тело цикла
    действие

Примеры использования:
"""
# Перебор элементов списка
# fruits = ["яблоко", "банан", "вишня"]
# for fruit in fruits:
#     print(fruit)  # Выведет каждый фрукт в списке

# Перебор символов строки
# for char in "Python":
#     print(char)  # Выведет каждый символ строки


# range()
"""
Функция range() генерирует последовательность чисел.
Синтаксис:
    range(start, stop, step)

- start (необязательно) - начальное значение (по умолчанию 0)
- stop - конечное значение (не включается в диапазон)
- step (необязательно) - шаг (по умолчанию 1)

Примеры:
"""
# print(list(range(5)))       # [0, 1, 2, 3, 4]
# print(list(range(2, 8)))    # [2, 3, 4, 5, 6, 7]
# print(list(range(1, 10, 4)))  # [1, 4, 7]  [1,2,3,4,5,6,7,8,9]
# print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

# Перебор чисел с помощью range()
# for i in range(1, 6):
#     print(i)  # Выведет числа от 1 до 5

# Использование range() с шагом
# for i in range(2, 10, 2):
#     print(i)  # Выведет 2, 4, 6, 8


# Вложенные циклы
"""
Вложенные циклы позволяют перебирать при этом другую последовательность внутри.

Пример: Вывести построчно таблицу умножения до 5x5.
"""
# 1,2,3,4
# 1,2,3,4
# 1,2,3,4
# 1,2,3,4
# print(i, end="\t")  # end именованный аргумент по дефолту установлен в /n(переход вывода на новую строку)


# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(0, 10):
#             print(k, end="\t")
#         print()  # Новая строка после каждого ряда


# Цикл while
"""
Цикл while выполняется, пока заданное условие истинно.
Синтаксис:

while условие:
    # тело цикла
    действие

Пример:
"""
# x = 1
# while x < 10:
#     print(x)
#     x += 1  # Уменьшаем x на 1
# got_message = False
# while not got_message:
#     print("Waiting for message...")
#     response = input("Input message: ")
#     if response != "":
#         got_message = True
#         print("Got message:", response)


# ОЗНАКОМИТЕЛЬНЫЕ ЗАДАЧИ (10 задач)

# 1. Выведите числа от 1 до 10 с помощью for
# numbers = (1,2,3,4,5,6,7,8,9,10)
# for number in numbers:
#     print(number)
# 2. Выведите числа от 10 до 1 с помощью while
# num = 10
# while num >= 1:
#     print(num)
#     num -= 1

# 3. Выведите все чётные числа от 2 до 20
# for list in range(2, 20, 2):
#     print(list)

# 4. Найдите сумму чисел от 1 до 100


# 5. Запросите у пользователя число и выведите его факториал
# n = int(input("Введите число:  "))
# factorial = 1
# for i in range(1, 1 + n):
#     print(i)  # Не поняла как вывести факториал

# 6. Используйте while, чтобы вывести квадраты чисел от 1 до 10
# n = 1
# while n <= 10:
#     print(n ** 2)
#     n += 1

# 7. Найдите сумму всех нечётных чисел от 1 до 50
# total_sum = 0
# for i in range(1, 51):
#     if i % 2 != 0:
#         total_sum += 1
#
# print(total_sum)


# 8. Используйте цикл for, чтобы вывести символы строки "Python"
# for letter in "Python":
#     print(letter)

# 9. Создайте список чисел и найдите их среднее значение
# numbers = 89, 72, 45, 79
# sum_numbers = 0
# count_numbers = 0
# for num in numbers:
#     sum_numbers += num
#     count_numbers += 1



# 10. Напишите программу, которая запрашивает у пользователя числа, пока он не введёт 0
# number = int(input("Введите число для входа: "))
# while number != 0:
#     print(number)



# ДОМАШНЕЕ ЗАДАНИЕ (40 задач)

# 11. Выведите таблицу умножения на 5

# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(0, 10):
#             print(k, end="\t")
#         print()

# 12. Выведите все числа кратные 3 от 1 до 100
# for i in range(1, 101):
#     if i % 3 == 0:
#         print(i)

# 13. Запросите у пользователя число и выведите его таблицу умножения
# number = int(input("Введите число: "))
# for i in range(1, 11):
#     print(i * number)

# 14. Найдите сумму всех чисел от 1 до N (N вводит пользователь)
# n = int(input("Введите число:"))
# summ = 0
# for i in range(1, n):
#     summ += i
#     print(summ)

# 15. Выведите числа Фибоначчи до 100

# lst = [0, 1]
# for i in range(2, 101):
#     lst.append(lst[i - 2] + lst[i - 1])
# print()

# 16. Проверьте, является ли введённое число простым


# 17. Переверните строку, введённую пользователем
# tmp = ""
# str1 = input("Enter a string: ")
# for i in range(len(str1) -1, -1, -1):
#     tmp += str1[i]
# print(tmp)

# 18. Посчитайте количество гласных букв в строке
# count_vowels = 0
# str2 = input("Enter word: ")
# vowels = ["a", "i", "e", "o", "u", "y"]
# for i in str2:
#     if i in vowels:
#         count_vowels += 1
# print(count_vowels)

# 19. Посчитайте сумму цифр числа
# numbers = int(input("Enter number: "))
# sum_numbers = 0
# for num in numbers:
#     sum_numbers += num
#     print(sum_numbers)  #Выводит ошибку  'int' object is not iterable

# 20. Запросите у пользователя строку и выведите её без гласных

# text = input("Enter sentence: ")
# vowels = ["a", "e", "i", "o", "y"]
# sentence = ""
# for char in text:
#     if char not in vowels:
#         sentence += char
# print(sentence)

# 21. Сгенерируйте список из 10 случайных чисел и выведите их среднее значение
# numbers = [10, 30, 45, 76, 98, 35, 20, 16]
# sum_numbers = 0
# for num in numbers:
#     sum_numbers += num
#
# average = sum_numbers/ len(numbers)
#
# print("List of numbers:", numbers)
# print("Average if numbers: ", average)

# 22. Определите, является ли введённая строка палиндромом
# string = input("Введите строку: ")
# reversed_text = string[::-1]
# palindrome = True
# for i in range(len(string)):   #Не поняла как дальше вывести

# 23. Используйте while для создания обратного отсчёта от 10 до 1
# x = 10
# while x >= 1:
#     print(x)
#     x -= 1
# 24. Выведите квадраты всех чётных чисел от 1 до 50
# for number in range(1, 51):
#     if number % 2 == 0:
#         print(number ** 2)
# 25. Найдите максимальное число в списке
# numbers = [8, 9, 5, 60, 12]
# max_numbers = numbers[0]
# for num in numbers:
#     if num > max_numbers:
#         max_numbers = num
#         print(num)

# 26. Выведите все пары чисел от 1 до 10, сумма которых равна 10
# for i in range (1, 10):
#     for j in range(1, 10):
#         if i + j == 10:
#             print(i, j)

# 27. Запросите у пользователя 5 чисел и выведите их среднее
# total = 0
# for i in range(5):
#     numbers = int(input("Введите 5 чисел: "))
#     numbers = numbers.split()
#     total += numbers
# average = total / 5
# print(average)  #Почему он не выводит список чисел, выводит

# 28. Используйте цикл while, чтобы угадать число, загаданное программой
# num = int(input("Enter number: "))


# 29. Сгенерируйте таблицу квадратов чисел от 1 до 10
# for i in range(1, 11):
#     square= i ** 2
#     print(square)

# 30. Найдите количество чётных и нечётных чисел в списке

# even_number = 0
# odd_number = 0
# for num in range(1, 100):
#     if num % 2 == 0:
#         even_number += 1
#     else:
#         odd_number += 1
#
# print("Количество четных чисел", even_number)
# print("Количество не четных чисел", odd_number)

# 31. Определите наибольший общий делитель (НОД) двух чисел
a = 15
b = 89


# 32. Найдите все простые числа в диапазоне от 1 до 100
# 33. Создайте список из первых 10 чисел Фибоначчи
# 34. Подсчитайте, сколько раз встречается определённая буква в строке
# 35. Найдите сумму элементов списка, которые больше 10
# 36. Проверьте, являются ли два введённых слова анаграммами
# 37. Создайте программу, которая заменяет все пробелы в строке на подчеркивания
# 38. Определите, сколько раз в строке встречается определённое слово
# 39. Напишите программу, которая считает, сколько раз в строке встречаются цифры
# 40. Используйте цикл while, чтобы находить сумму вводимых пользователем чисел, пока он не введёт "стоп"

