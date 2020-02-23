# https://drive.google.com/open?id=1MhZu31Ru0xWY7eHmbyUZb974EgyPUXYX
print('Введите число от 1 до 26:')
num = int(input())
alphabet = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H',
            9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
            16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V',
            23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
if num in alphabet:
    print(f"В алфавите под номером {num} находится буква {alphabet[num]}.")
else:
    print(f'В алфавите нет буквы с номером {num}.')
