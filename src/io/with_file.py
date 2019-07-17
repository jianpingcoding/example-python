# -*- coding: utf-8 -*-

# One Statement per Line
from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('Today is ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

# A single line should not exceed the number of 79 characters
with open('test1.txt') as file_1, \
     open('test2.txt', 'w') as file_2:
    file_2.write(file_1.read())
