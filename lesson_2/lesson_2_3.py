# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# https://drive.google.com/open?id=1iFhaFrAzWSLYvLHldWOVN8CSHM9m_9j5

num = int(input('Введите целое положительное число: '))


def funk(n):
    x = n % 10
    n = int(n / 10)
    if n != 0:
        return f'{x}{funk(n)}'
    else:
        return f'{x}'


z = funk(num)

print(z)
