# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

NUMBER_OF_COLUMNS = 4
NUMBER_OF_LINES = 5

matrix = [['_'] * NUMBER_OF_COLUMNS for _ in range(NUMBER_OF_LINES)]

for i in range(NUMBER_OF_LINES):
    print(f'Ведите цыфры строки номер: {i + 1}')
    matrix[i][-1] = 0
    for o in range(NUMBER_OF_COLUMNS - 1):
        matrix[i][o] = int(input(f'Ведите целое число столбца номер {o + 1}:'))
        matrix[i][-1] += matrix[i][o]

print('Итоговая матрица:')
print(*matrix, sep='\n')