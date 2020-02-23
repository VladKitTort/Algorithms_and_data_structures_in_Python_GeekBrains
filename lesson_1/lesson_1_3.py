# https://drive.google.com/open?id=1bRfwVCiMgfVXtfXv7LYo5cptuj92BXnY
print("Введите координаты точки A(x1; y1):")
x1 = float(input("\tx1 = "))
y1 = float(input("\ty1 = "))

print("Введите координаты точки B(x2; y2):")
x2 = float(input("\tx2 = "))
y2 = float(input("\ty2 = "))

if x1 == x2:
    print('Делить на 0 нельзя.')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    print(" y = %.2f*x + %.2f" % (k, b))
