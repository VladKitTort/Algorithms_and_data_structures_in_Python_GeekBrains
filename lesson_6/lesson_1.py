# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

"""
- Оптимальным вариантом считаю функцию mix_2, так как по итоговым замерам использует меньше всего памяти.
- У меня ноутбук с Windows 10 64 разрядная, Python так же 64 разрядный.
        Первый вариант занимает памяти:379666 байт
        Второй вариант занимает памяти: 371909 байт
        Третий вариант занимает памяти: 375876 байт
- Максимальная разница между значениями (второй и первый варианты) в 2%. Что в принципе не особо критично, но я бы еще
    отметил размерность кода, и считаю что второй вариант так же является более локаничным в сравнении с первым
    вариантом.
- Второй вариант кода вышел победителем.
"""
from sys import getsizeof
from random import randint


def show(obj):
    sum_bit = getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                sum_bit += show(key)
                sum_bit += show(value)
        elif not isinstance(obj, str):
            for item in obj:
                sum_bit += show(item)
    return sum_bit


def mix_1(matrix):  # Первый вариант занимает памяти:379666 байт
    min_column_value = []
    for i in range(SIZE):
        column = []
        for o in range(SIZE):
            column.append(matrix[o][i])
        num_min = column[0]
        for p in column:
            if num_min >= p:
                num_min = p
        min_column_value.append(num_min)
    max_num_min_column_value = min_column_value[0]
    for i in min_column_value:
        if max_num_min_column_value <= i:
            max_num_min_column_value = i
    lol = locals()
    return show(lol)


def mix_2(matrix):  # Второй вариант занимает памяти: 371909 байт
    max_ = None
    for j in range(len(matrix[0])):
        min_ = matrix[0][j]
        for i in range(len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]
        if max_ is None or max_ < min_:
            max_ = min_
    lol = locals()
    return show(lol)


def mix_3(matrix):  # Третий вариант занимает памяти: 375876 байт
    max_ = float('-inf')
    res_arr = []
    for y in range(SIZE):
        min_ = float('inf')
        for x in range(SIZE):
            if min_ > matrix[x][y]:
                min_ = matrix[x][y]
        res_arr.append(min_)
    for el in res_arr:
        if max_ < el:
            max_ = el
    lol = locals()
    return show(lol)


SIZE = 100
MIN_ITEM = -10000
MAX_ITEM = 100000
dom_1 = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]
dom_2 = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]
dom_3 = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]

print(f'Первый вариант занимает памяти:'
      f'{mix_1(dom_1)} байт')
print(f'Второй вариант занимает памяти: '
      f'{mix_2(dom_2)} байт')
print(f'Третий вариант занимает памяти: '
      f'{mix_3(dom_3)} байт')

