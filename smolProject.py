# def sum_function():
#     result = 'I\'m good'
#     return result

def show_message():
    message = 'type "hi" or "hello" in the input'
    print(message)
    user_input = input('\nhi or hello?: ')
    return user_input

def options(user_input):
    if user_input == 'hi':
        # sum_function()
        print('hi, how are you?')
        options(show_message())
    else:
        print('wrong input')

welcome = 'type "hi" or "hello"'
print(welcome)
user_input = input('\nhi or hello?: ')

if user_input == 'hi':
    # sum_function()
    print('hi, how are you?')
    options(show_message())

def my_function(**names):  
  print("My name is ", names["fname"], names["lname"])  
my_function(fname = "Daksh", lname = "Lal")

def hello(a, b):
    check = lambda a,b: a * b
    print('\nMultiply: ', check(a,b))

hello(10,20)