# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Стартовый массив: {array}')

num_min = array[0]
num_max = array[0]

for i in array:
    if num_min >= i:
        num_min = i
    if num_max <= i:
        num_max = i

print(f'Минимальная цифра в массиве: {num_min}')
print(f'Максимальная цифра в массиве: {num_max}')

index_min = array.index(num_min)
index_max = array.index(num_max)

print(f'Индекс минимальной цифра в массива: {index_min}')
print(f'Индекс максимальная цифра в массива: {index_max}')

array[index_min], array[index_max] = array[index_max], array[index_min]

print(f'Итоговый массив: {array}')

