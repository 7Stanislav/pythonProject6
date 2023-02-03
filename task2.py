"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
Реализуйте с list comprehension
"""

from random import randint
numbers = [randint(0, 301) for i in range(13)]
print(f"Пример исходного списка: {numbers}")
new_list = [el for num, el in enumerate(numbers) if numbers[num - 1] < numbers[num]]
print(new_list)
