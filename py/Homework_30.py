# Q2
def odd_even_id(user_input):         #creating/defining a function
    if user_input == 0:              #adding a condition to check if arg(r) is 0 print num is even else print odd
        print('input is even')
    else:
        print('user input is odd')

u_input = int(input('\nenter a number: '))  #asking user for input
r = int(u_input) % 2                        # using modulo to get remainder
odd_even_id(r)                              #calling the function with arg 'r' which can be 0 or 1

#Q3

def table(my_input):                      #defining a function
    if type(my_input) == int:             #adding condition to check if arg is an integer then printing the stuff below
        print('input is valid, processing........')
    else:
        print('error: invalid number')
        

m_input = int(input('enter a number: '))      #asking for user input

table(m_input)                            #calling function

i = 1                                     #initializing loop by assigning i w a value
while i < 11:                             #adding a condition in while loop
    m = m_input * i                       #multiplies input with i
    print(m)                              #prints m
    i += 1                                #increments i by 1


# Q1
# TYPE 1 ASKING USER WHICH OPERATION THEY WANTS TO DO
# asking user for input
dig1 = input('enter first number: ')
dig2 = input('enter second number: ')
dig3 = input('enter third number: ')
dig4 = input('enter fourth number: ')

t = [int(dig1), int(dig2) , int(dig3) , int(dig4)]
print('your input = ' ,t)

def calc(hello):                                                    #defining function (with arg without return)
    if hello == '+':                                                #if arg is + adds all the inputs
        r1 = int(t[0]) + int(t[1]) + int(t[2]) + int(t[3])
        print('result = ', r1)     
    elif hello == '*':                                              #if arg is * multiplies all inputs
        r2 = int(t[0]) * int(t[1]) * int(t[2]) * int(t[3])
        print('result = ', r2)
    elif hello == '-':                                              #if arg is - subtracts all inputs
        r3 = int(t[0]) - int(t[1]) - int(t[2]) - int(t[3])
        print('result = ', r3)
    else:                                                           #if above conditions fail print this
        print('invalid operation, try again')

#giving user options on what he can do
print('''
    PRESS + TO ADD
    PRESS * TO MULTIPLY
    AND - TO SUBTRACT
     ''')
hello = input('what would you like to do?: ')                   #asking user which operation to perform
calc(hello)                                                     #calling function

#TYPE 2 DOING ALL OPERATIONS WITHOUT USER INPUT

#asking for user input
dig1 = input('enter first number: ')
dig2 = input('enter second number: ')
dig3 = input('enter third number: ')
dig4 = input('enter fourth number: ')

t = [int(dig1), int(dig2) , int(dig3) , int(dig4)]                                  # storing input data in a list
print('\nyour input = ' ,t)                                       #prints input in a list

def auto_calc(t):                                               # defining a function (with arg wo return)
    r1 = int(t[0]) + int(t[1]) + int(t[2]) + int(t[3])          #adding everything
    print('result = ', r1)                                      #print result
    r2 = int(t[0]) * int(t[1]) * int(t[2]) * int(t[3])          #multiplying everything
    print('result = ', r2)                                      #print result
    r3 = int(t[0]) - int(t[1]) - int(t[2]) - int(t[3])          # subtracting everything
    print('result = ', r3)                                      # print result
    yo = [r1, r2, r3]
    print('result in a list', yo)

auto_calc(t)                                                    #calling function


    