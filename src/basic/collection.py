# -*- coding: utf-8 -*-

# list, Indentation
langs = [
    'Python',
    'Java',
    'Swift'
]
for lang in langs:
    print(lang)

# tuple
company_names = (
    'Google',
    'Apple',
    'Amazon'
)
print('len(company_names) =', len(company_names))  # 3
print('company_names[0] =', company_names[0])  # Google
print('company_names[-1] =', company_names[-1])  # Amazon

# set
fruits = {'apple', 'banana', 'cherry'}
print(fruits)
first_number_set = set([1, 1, 2, 3, 3])
print(first_number_set)  # {1, 2, 3}
second_number_set = set([2, 3, 4])
print(first_number_set & second_number_set)  # {2, 3}
print(first_number_set | second_number_set)  # {1, 2, 3, 4}

# dictionary
person = {
    'name': 'Johnny',
    'age': 30
}
print('person[\'name\'] =', person['name'])
print('person.get(\'age\', -1) =', person.get('age', -1))

for x in range(10):
    print(x)
