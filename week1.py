#Function with default values
def add_numbers(x = 0, y = 0, z = 0):
    return x + y + z

x = 1
y = 1
z = 1

print(add_numbers(x, y))

#Another function with default values
def do_math(a = 0, b = 0, kind = 'add'):
    if (kind == 'add'):
        return a + b
    else:
        return a - b

print(do_math(1, 2))

#Tuples
x = (1, 'a', 2, 'b')
print(type(x))
try:
    x[0] = 3
except:
    print("Tuples are immutable")


for item in x:
    print(item)

#Strings
x = [0, 'a', 1, 'b']
print(type(x))
x[0] = 3
print(x)

y = [2, 'c']
print(x + y)
print(x * 2)
print('c' in y)
print(x[1:4])
print(x[-1:])

string = "Dogs dogs hotdogs"
print("dog" in string)
print(string.split(' '))

#Dictionaries
x = {0: 'a', 1: 'b'}
print(x[1])
x[1] = 'c'
print(x[1])

for keys,values in x.items():
    print(keys)
    print(values)

#Unpacking tuple
x = ('a', 'b', 'c')
a, b, c = x
print(a)
print(b)
print(c)

print('name' + str(2))

#String formatting
sales_record = {'price': 3.23, 'num_items': 4, 'person': 'chris'}
sales_statement = '{} bought {} item(s) at price of {} each for a total of {}'
print(sales_statement.format(sales_record['person'], sales_record['num_items'], sales_record['price'], sales_record['price'] * sales_record['num_items']))

#Using lambda to make small functions
my_function = lambda a, b, c: a + b
print(my_function(1, 2, 3))

people = ['Dr. A', 'Dr. B', 'Dr. C', 'Dr. D']

def split_title_and_name(person):
    return person.split()[0] + '\n' + person.split()[-1]

print(split_title_and_name(people[0]))
for person in people:
    z = lambda x: x.split()[0] + '\n' + x.split()[-1]
    print(z(person))

print(list(map(split_title_and_name, people)))
print(list(map(lambda x: x.split()[0] + '\n' + x.split()[-1], people)))

#list comprehension
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)

my_list = [number for number in range(0, 1000) if number % 2 == 0]
print(my_list)

import numpy as np

x = [i for i in range(0, 36)]
x = np.asmatrix(x).reshape((6, 6))
print(x)
print(x[2:4, 2:4])
x = x.reshape(36)
print(x[0,::7])

