# -*- coding: utf-8 -*-

import random

x = 1  # int
y = 2.8  # float
z = 1j  # complex
print(type(z))
a = float("3")  # 3.0
b = int(2.8)  # 2
c = complex(z)
print(random.randrange(1, 10))

age = int(input('Input your age: '))
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)
