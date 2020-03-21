from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE * 2 + 1)]


def asa(arr):
    length_array = range(len(arr) - 1)
    while True:
        for i in (length_array, reversed(length_array)):
            one_more_time = 0
            for n in i:
                if arr[n] > arr[n + 1]:
                    arr[n], arr[n + 1] = arr[n + 1], arr[n]
                    one_more_time = 1
            if one_more_time == 0:
                return arr


print(f'\nСтартовый массив данных: {array}')
print(f'\nОтсортированный массив данных: {asa(array)}')
print(f'\nМеридиана массива данных: {array[SIZE]}')
