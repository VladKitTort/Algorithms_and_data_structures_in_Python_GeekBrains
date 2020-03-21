from random import randint

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]


def bubbles(arr):
    n = True
    while n:
        n = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                n = True
    return arr


print(array)
print(bubbles(array))

