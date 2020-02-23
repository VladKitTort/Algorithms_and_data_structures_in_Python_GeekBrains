# https://drive.google.com/open?id=1uvwtEpGU1xSQPS5qh7HjOJswfIjB-tmh
print("Ведите челое трех значное число:")
x = int(input())
a = x % 10
b = x // 10
b = b % 10
c = x // 100
y = a + b + c
z = a - b - c
print(y)
print(z)