
# Урок 9: Кортежи и множества — основные операции

# 1. **Что такое кортеж (tuple)**:
#    - Кортеж — это неизменяемая структура данных, аналог списка, но с фиксированным размером.
#    - Неизменяемость означает, что после создания кортеж нельзя изменить (добавить, удалить или изменить элементы).
#    - Объявление кортежей:

# Объявление(создание, инициализация) кортежей:
# my_tuple = (1, 2, 3)
# aaadfasdfadsf = (2, 2, 11, 234)
# aaadfasdfadsf = 1
# single_element_tuple = (5,)  # Обратите внимание на запятую — так создается кортеж из одного элемента
#
# # - Доступ по индексу:
# print(my_tuple[0])  # Вывод: 1
#
# # - Вложенные кортежи (кортежи внутри кортежей):
# nested_tuple = (1, (2, 3), (4, 5))
# print(nested_tuple[1][0])  # Вывод: 2
#
# # - Преобразование списка в кортеж и наоборот:
# list_to_tuple = tuple([1, 2, 3])
# tuple_to_list = list((1, 2, 3))

# - Преимущества кортежей перед списками:
# - Быстрее обрабатываются, так как неизменяемы.
# - Могут использоваться как ключи в словарях (в отличие от списков).

# # 2. **Основные методы кортежей**:
# #    - `count(value)` — количество вхождений значения:
# my_tuple = (1, 2, 2, 3, 2)
# print(my_tuple.count(2))  # Вывод: 3
#
# # - `index(value)` — индекс первого вхождения значения:
# print(my_tuple.index(2))  # Вывод: 1
#
#
# # 3. **Что такое множество (set)**:
# #    - Множество — это неупорядоченная коллекция уникальных элементов.
# #    - Не допускает дубликатов и изменяемо (можно добавлять и удалять элементы).
# #    - Создание множества:
#
#
# my_set = {1, 2, 3}
# my_set_from_list = set([1, 2, 3])  # int() str() bool()
# print(my_set_from_list)  # Вывод: {1, 2, 3}
#
# # - Преобразование списка или строки в множество:
# set_from_string = set('hello')
# print(set_from_string)  # Вывод: {'h', 'e', 'l', 'o'}
#
# # 4. **Основные методы множеств**:
# #    - `add(value)` — добавление элемента:
# my_set.add(4)
# print(my_set)  # {1, 2, 3, 4}
#
# # - `remove(value)` — удаление элемента (ошибка, если не найден):
# my_set.remove(2)
#
# # - `discard(value)` — удаление элемента (без ошибки, если не найден):
# my_set.discard(10)  # Ошибки не будет, даже если 10 нет в множестве
#
# # - `pop()` — удаление случайного элемента:
# removed = my_set.pop()
# print(removed)  # Удалит и вернет случайный элемент
#
# # - `clear()` — очистка множества:
# my_set.clear()
# print(my_set)  # Пустое множество: set()
#
# # - `union()`, `intersection()`, `difference()`, `symmetric_difference()`:
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.union(set2))             # {1, 2, 3, 4, 5}
# print(set1.intersection(set2))      # {3}
# print(set1.difference(set2))        # {1, 2}
# print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}
#
# # 5. **Операции над множествами**:
# #    - Проверка принадлежности:
# print(2 in set1)       # True
# print(5 not in set1)   # True
#
# # - Подмножество и надмножество:
# subset = {1, 2}
# superset = {1, 2, 3, 4}
# print(subset < superset)   # True — subset является подмножеством superset
# print(superset > subset)   # True — superset является надмножеством subset
# print(subset <= superset)  # True — неполное или полное подмножество
# print(superset >= subset)  # True — неполное или полное надмножество

# Кортежи — это неизменяемые и быстрые структуры данных, которые используются там, где важна постоянность данных.
# Множества позволяют эффективно работать с уникальными элементами, проверять принадлежность и выполнять операции
# пересечения и объединения.
# Используйте кортежи для неизменяемых последовательностей, а множества — для уникальных коллекций элементов.


# Ознакомительные задачи:

# 1. Создай кортеж из трёх чисел и выведи сумму всех элементов.
# new_tuple = (78, 53, 24)
# print(sum(new_tuple))

# 2. Напиши программу, которая проверяет, есть ли определённое значение в кортеже.
#
# print(78 in new_tuple)

# 3. Создай кортеж из строк и объедини их в одну строку через пробел.
text = ("asus", "table", "flowers", "laptop", "spoon", "mouse")
one_text = " ".join(text)
print(one_text)

# 4. Создай кортеж с числами и найди максимальное и минимальное значение.

# numbers = (67, 89, 53)
# print(max(numbers))
# print(min(numbers))

# 5. Преобразуй список ['apple', 'banana', 'cherry'] в кортеж.
fruits = tuple(["apple", "banana", "cherry"])
print(fruits)

# 6. Напиши программу, которая принимает список чисел и возвращает кортеж только из уникальных значений.
numbers = input("Введите числа: ")
unique_numbers = set(numbers)
print(tuple(numbers))

# 7. Создай множество с числами от 1 до 5 и добавь к нему число 6.

# 8. Удали элемент "banana" из множества {'apple', 'banana', 'cherry'}.
# 9. Найди пересечение множеств {1, 2, 3} и {2, 3, 4}.
# 10. Определи, является ли множество {1, 2} подмножеством множества {1, 2, 3, 4}.


# Домашнее задание (40 задач):

# 1. Создай кортеж из трёх случайных строк и проверь, содержится ли в нём строка "Python".
# 2. Преобразуй строку "hello world" в кортеж символов.
# 3. Даны два кортежа: (1, 2, 3) и (4, 5, 6). Объедини их в один.
# 4. Создай кортеж чисел и посчитай количество вхождений числа 5.
# 5. Даны два кортежа. Проверь, совпадает ли первый элемент первого кортежа с последним элементом второго.
# 6. Напиши программу, которая меняет местами первый и последний элемент кортежа.
# 7. Создай пустое множество и добавь в него три уникальных числа.
# 8. Удали произвольный элемент из множества {10, 20, 30, 40}.
# 9. Создай множество из строки "abracadabra" и выведи уникальные символы.
# 10. Объедини множества {1, 2, 3} и {3, 4, 5}.
# 11. Проверь, являются ли множества {1, 2, 3} и {3, 2, 1} равными.
# 12. Создай множество с числами от 1 до 10 и удали все чётные числа.
# 13. Напиши программу, которая проверяет, есть ли пересечение у множеств {1, 2, 3} и {4, 5, 6}.
# 14. Дан кортеж чисел. Выведи все элементы, кроме первого и последнего.
# 15. Проверь, может ли кортеж (1, 2, 3) быть ключом словаря.
# 16. Создай кортеж и преобразуй его в строку через запятую.
# 17. Найди количество уникальных символов в строке "datascience" с использованием множества.
# 18. Создай множество из списка чисел [1, 2, 2, 3, 4, 4, 5] и выведи его длину.
# 19. Напиши программу, которая возвращает разность множеств {1, 2, 3} и {2, 3, 4}.
# 20. Дан кортеж чисел. Найди сумму всех элементов, не используя встроенную функцию sum().
# 21. Создай множество из чисел от 1 до 5 и проверь, является ли число 3 элементом множества.
# 22. Найди длину кортежа (10, 20, 30, 40).
# 23. Создай кортеж, содержащий 5 одинаковых элементов.
# 24. Дан кортеж с числами. Найди индекс первого отрицательного числа.
# 25. Напиши программу, которая проверяет, можно ли преобразовать множество {1, 2, 3} в неизменяемое множество (frozenset).
# 26. Проверь, является ли множество {1, 2} подмножеством {1, 2, 3, 4}.
# 27. Напиши программу, которая возвращает симметрическую разность множеств {1, 2, 3} и {3, 4, 5}.
# 28. Создай кортеж и найди индекс первого вхождения числа 7.
# 29. Напиши программу, которая создаёт множество из всех символов строки "python" и удаляет из него символ 'h'.
# 30. Проверь, является ли множество {1, 2, 3} надмножеством {2, 3}.
# 31. Создай кортеж и попытайся изменить его элемент (ожидай ошибку).
# 32. Напиши программу, которая находит общие элементы в кортежах (1, 2, 3) и (2, 3, 4).
# 33. Создай множество из чисел и удали из него минимальное значение.
# 34. Преобразуй кортеж (1, 2, 3) в список и добавь к нему число 4.
# 35. Создай кортеж из случайных чисел и отсортируй его (без изменения оригинала).
# 36. Напиши программу, которая проверяет, есть ли пересечение у множеств {1, 2, 3} и {4, 5, 6}.
# 37. Создай кортеж из строк и найди самую длинную строку.
# 38. Преобразуй кортеж в множество и найди его длину.
# 39. Найди минимальный элемент множества {10, 20, 5, 30}.
# 40. Создай множество и добавь в него все буквы строки "data" и "science" без повторений.
