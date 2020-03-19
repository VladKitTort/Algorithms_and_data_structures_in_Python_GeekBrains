import collections


def sum_16(n):
    list_of_numbers = collections.deque([str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F'])
    if len(n[0]) < len(n[1]):
        n.reverse()
    sum_result = []
    p = -1
    k = 0
    for i in n[1][::-1]:
        number_1 = list_of_numbers.index(i)
        number_2 = list_of_numbers.index(n[0][p])
        sum_result.append(list_of_numbers[(number_1 + number_2 + k) % 16])
        if (number_1 + number_2) >= 15:
            k = 1
        else:
            k = 0
        p -= 1
        if p == -len(n[0]) - 1:
            break
    length = len(n[0]) - len(n[1])
    while length > 0:
        sum_result.append(list_of_numbers[(list_of_numbers.index(n[0][length - 1]) + k) % 16])

        if list_of_numbers.index(n[0][length - 1]) + 1 > 15:
            k = 1
        else:
            k = 0
        length -= 1
    if k == 1:
        sum_result.append('1')
    sum_result.reverse()
    return sum_result


num_1 = list(input("Введите первое число в 16 системе исчисления: ").upper())
num_2 = list(input("Введите воторое число в 16 системе исчисления: ").upper())
print(sum_16(collections.deque([num_1, num_2])))

