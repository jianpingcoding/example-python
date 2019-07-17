"""
Python string
"""
# -*- coding: utf-8 -*-

print('The quick brown fox', c'jumps over', 'the lazy dog')


s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))


x = "Salary"  # x is now of type str
# String variables can be declared either by using single or double quotes
x = 'Salary # '
# you can assign the same value to multiple variables in one line
x = y = z = "Banana"
x, y, z = 'Orange', 'Banana', 'Kiwi'
z = x + y
print(z)

long_str = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit."""
print(long_str[1])  # String are arrays
print(long_str[2:5])  # Get the characters from position 2 to position 5

hello_world = " Hello, World! "
# removes any whitespace from the beginning or the end
print(hello_world.strip())
print(len(hello_world))
print(hello_world.lower())
print(hello_world.upper())
print(hello_world.replace("H", "J"))
print(hello_world.split(","))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

x = str(3.0)  # '3.0'
