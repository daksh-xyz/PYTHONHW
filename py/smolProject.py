# # def sum_function():
# #     result = 'I\'m good'
# #     return result
# fileName = input('enter fileName loser: ') 
# if 'daksh' in fileName:
#     print('loser')

# def show_message():
#     message = 'type "hi" or "hello" in the input'
#     print(message)
#     user_input = input('\nhi or hello?: ')
#     return user_input

# def options(user_input):
#     if user_input == 'hi':
#         # sum_function()
#         print('hi, how are you?')
#         options(show_message())
#     else:
#         print('wrong input')

# welcome = 'type "hi" or "hello"'
# print(welcome)
# user_input = input('\nhi or hello?: ')

# if user_input == 'hi':
#     # sum_function()
#     print('hi, how are you?')
#     options(show_message())

# def my_function(**names):  
#   print("My name is ", names["fname"], names["lname"])  
# my_function(fname = "Daksh", lname = "Lal")

# def hello(a, b):
#     check = lambda a,b: a * b
#     print('\nMultiply: ', check(a,b))

# hello(10,20)

# import numpy as np
# numpy = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(numpy)

import numpy as np
from random import choice
a = int(input('rows: '))
b = int(input('columns: '))
arr = ['1','2','3','4','5','6','7','8']

c = a * b

print(len(arr))
if len(arr) < c:
    k = len(arr)
    while k != c:
        x = choice(['/', '|', '#'])
        y = arr.append(x)
        k += 1

z = np.array(arr).reshape(a,b)
print(z)