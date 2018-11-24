#Составить программу нахождения корней квадратного уравнения в общем виде. Коэффициенты запрашиваются у пользователя.
from math import sqrt
a = int(raw_input('a = '))
b = int(raw_input('b = '))
c = int(raw_input('c = '))
x1 = int((-b+sqrt(b/4*a*c))/2*a)
x2 = int((-b-sqrt(b/4*a*c))/2*a)
print(x1, x2)
