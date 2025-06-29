# === Урок 19: Модули и пакеты ===

# 🔹 Что такое модуль?
# Модуль — это файл с кодом на Python, который можно импортировать в другие файлы.
# Каждый файл .py — это модуль.

# Пример создания модуля:
# В файле math_utils.py:
# def add(a, b):
#     return a + b

# В другом файле:
# import math_utils # загружает весь файл(модуль), все функции, переменные
# from math_utils import * # загружает весь файл(модуль), все функции, переменные

# print(math_utils.add(2, 3))  # Вывод: 5
# print(math_utils.sub(2, 3))

from math_utils import add, sub

# print(add(2, 3))  # Вывод: 5
# print(sub(2, 3))

# 🔹 Способы импорта модулей:

# 1. import module
# import math
# print(math.sqrt(16))

# 2. from module import function
# from math import sqrt
# print(sqrt(25))

# 3. from module import *  (не рекомендуется)
# from math import *
# print(sqrt(36))

# 4. import module as alias
# import math as m
# print(m.sqrt(49))

# 🔹 Встроенные (стандартные) модули:
# import random, datetime, os, sys, json
#
# print(random.randint())
# print(datetime.datetime.now())
# print(os.path.pardir)
# print(sys.path)

# 🔹 Установка сторонних модулей:
# pip install requests

# 🔹 Что такое пакет?
# Пакет — это папка с файлами Python и файлом __init__.py
# Пример:
# my_package/
# ├── __init__.py
# ├── module1 6.py
# └── module2.py

# Пример использования:
# from my_package import module1 6

# 🔹 Проверка пути к модулям:
# from my_package import module1
#
# print(module1.add(2, 5))
# #
# import sys
# print(sys.path)

# 🔹 Создание собственного пакета:
# - Создай папку
# - Добавь туда модули
# - Вставь __init__.py
# - Используй from имя_пакета import модуль

# --- Ознакомительные задачи (10) ---

# 1. Импортируй модуль math и выведи квадратный корень из 64.
# import math
# print(math.sqrt(64))

# 2. Импортируй только функцию sqrt из модуля math и вычисли sqrt(81).
# from math import sqrt
# result = sqrt(81)
# print(result)

# 3. Используй псевдоним для math и вычисли косинус 0.
# import math as w
# result = w.cos(0)
# print(result)
# 4. Выведи текущую дату с помощью модуля datetime.
# from datetime import datetime
# print(datetime.now())

# 5. Импортируй модуль random и выбери случайное число от 1 до 100.
# import random
# print(random.randint(1, 100))
# 6. Используй модуль os, чтобы получить текущую директорию.
# import os
# print(os.getcwd())

# 7. Прочитай sys.argv из модуля sys.
# import sys
# print(sys.argv)


# 8. Импортируй json и преобразуй словарь в строку.
# import json
# maria = {
#     "name": "Мария",
#     "surname": "Морозов",
#     "birth_year": 1981
#   }
# dump = json.dumps(maria)
#
# print(type(dump))
#
# load =json.loads(dump)
#
# print(type(load))

# 9. Установи модуль requests и проверь его импорт.
# import requests
# print(requests)

# 10. Создай свой модуль с функцией say_hello() и используй его.
def say_hello()

# --- Домашнее задание (40 задач) ---

# 1. Создай функцию, которая импортирует модуль math и возвращает факториал числа 6.
# 2. Используй from math import sqrt и вычисли квадратный корень из 100.
# 3. Импортируй math как m и верни значение m.pi.
# 4. Используй random.randint для генерации числа от 50 до 150.
# 5. Выведи список всех атрибутов модуля math с помощью dir().
# 6. Получи текущую дату и время через datetime.datetime.now().
# 7. Создай функцию, которая возвращает только дату без времени.
# 8. Используй os.name, чтобы узнать операционную систему.
# 9. Выведи путь к текущему скрипту с помощью os.path.abspath(__file__).
# 10. Используй os.listdir() для просмотра содержимого текущей папки.

# 11. Используй sys.version для вывода версии Python.
# 12. Получи список путей поиска модулей с помощью sys.path.
# 13. Используй sys.exit() внутри функции (вызов закомментируй).
# 14. Сохрани словарь {'name': 'Ivan'} в JSON-строку.
# 15. Запиши словарь в файл data.json с помощью модуля json.
# 16. Прочитай JSON из файла и выведи имя пользователя.
# 17. Используй json.dumps() с отступами (indent=4).
# 18. Установи и импортируй emoji. Выведи смайл 😀.
# 19. Используй requests для запроса к https://api.github.com (нужен pip).
# 20. Считай JSON-ответ и выведи 'current_user_url'.

# 21. Создай свой модуль my_calc.py с функцией multiply(a, b).
# 22. Импортируй эту функцию в main.py и вызови multiply(3, 4).
# 23. Создай пакет my_utils/ с __init__.py и модулем tools.py.
# 24. В tools.py создай функцию greet(name). Импортируй и вызови её.
# 25. Прочитай текст из файла и раздели на строки в функции.
# 26. Получи список файлов в папке и отфильтруй только .txt.
# 27. Запиши список данных в файл, обернув всё в try/except.
# 28. Создай модуль string_utils.py с функцией reverse(text).
# 29. Проверь наличие файла 'config.txt'. Если нет — создай.
# 30. Получи имя пользователя через input() и сохрани в config.txt.

# 31. Напиши функцию, которая импортирует math и возвращает логарифм по основанию 10 от числа 1000.
# 32. Используй os.environ для вывода переменных окружения.
# 33. Создай функцию, которая возвращает количество файлов в папке.
# 34. Используй random.choice для выбора случайного элемента из списка.
# 35. Сериализуй список строк в JSON-файл.
# 36. Используй requests.get() для получения данных о погоде.
# 37. Установи модуль termcolor. Выведи текст цветом (пример: red).
# 38. Создай пакет calc/ с модулями add.py, sub.py. Импортируй их.
# 39. Реализуй импорт из модуля с абсолютным и относительным путём.
# 40. Подсчитай количество строк в файле script.py с использованием функций os и open().
