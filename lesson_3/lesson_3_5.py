# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

import random

SIZE = 2000000
MIN_ITEM = -1000000
MAX_ITEM = 1000000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Стартовый массив: {array}')

num = MIN_ITEM

for i in array:
    if num < i < 0:
        num = i
print(f'Максимальное отрицательное число в массиве {num}, и его индекс {array.index(num)}.')
