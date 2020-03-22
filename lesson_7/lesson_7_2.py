from random import randint

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 50
array = [randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]


def array_in_half(arr):
    if len(arr) < 2:
        return arr
    center = len(arr) // 2
    left_part = arr[:center]
    right_part = arr[center:]
    left_part = array_in_half(left_part)
    right_part = array_in_half(right_part)
    return sorting_parts(left_part, right_part)


def sorting_parts(left_part, right_part):
    result = []
    n = 0
    p = 0
    while n < len(left_part) and p < len(right_part):
        if left_part[n] <= right_part[p]:
            result.append(left_part[n])
            n += 1
        else:
            result.append(right_part[p])
            p += 1
    result += left_part[n:]
    result += right_part[p:]
    return result


print(array)
print(array_in_half(array))

