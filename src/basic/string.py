# -*- coding: utf-8 -*-
"""
Python string
"""


print('The quick brown fox', 'jumps over', 'the lazy dog')


chinese_str = 'Python-中文'
print(chinese_str)
encoded_chinese_str = chinese_str.encode('utf-8')
print(encoded_chinese_str)  # b'Python-\xe4\xb8\xad\xe6\x96\x87'
print(encoded_chinese_str.decode('utf-8'))  # Python-中文

normal_str = "Salary"  # x is now of type str
# String variables can be declared either by using single or double quotes
normal_str1 = 'Salary # '
# you can assign the same value to multiple variables in one line
x = y = z = "Banana"
x, y, z = 'Orange', 'Banana', 'Kiwi'
z = x + y
print(z) # OrangeBanana

long_str = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit."""
print(long_str[1])    # o, string are arrays
print(long_str[2:5])  # rem, get the characters from position 2 to position 5
print(long_str[2:5:2]) # rm, [start:stop:step]


hello_world = ' Hello, World! '
# removes any whitespace from the beginning or the end
print(hello_world.strip())
print(len(hello_world))
print(hello_world.lower())
print(hello_world.upper())
print(hello_world.replace('H', 'J'))
print(hello_world.split(','))
print(hello_world.index('o'))
print(hello_world.count('l'))
print(hello_world.startswith('Hello'))
print(hello_world.endswith('Hello'))
print(hello_world[::-1]) # !dlroW ,olleH

age = 36
txt = 'My name is John, and I am {}'
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

x = str(3.0)  # '3.0'
