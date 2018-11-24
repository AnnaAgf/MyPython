# Составить программу расчета гипотенузы прямоугольного треугольника. Длина катетов запрашивается у пользователя.
from math import sqrt
a = int(raw_input('catet 1 '))
b = int(raw_input('catet 2 '))
c = int(sqrt(a**2 + b**2))
print(c)
