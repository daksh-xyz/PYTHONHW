user_input = input('Enter a value: ')
print(user_input.__len__())
if user_input.strip().isdigit() == True:          #strip method removes a char from starting and ending, in our case it is removing '' which makes input a string 
    print('input number is an integer')   #is.digit tells if it is an integer in bool
    exit()                    # we use exit() because if it has identified the type of input we don't need it to identify it further/to stop code there

if user_input.strip().isdecimal() == True:       #checks if it is a decimal type integer
    print('input is floating point integer')
    exit()

if user_input.strip().isalpha() == True:         #checks if given input is alphabetical
    print('input is alphabetical')
    exit()

if user_input.strip().isalnum() == True:         #checks if input is alphanumerical -- placed here cuz if we place it first, recognizes alphabets and numbers as alphanum 
    print('input is alpha-numerical')
    exit()



Bio_data = {'name': input('\nEnter your name: '),
'age': int(input('\nEnter your age: ')),
'mobile': int(input('\nEnter your mobile number: ')),
'email': input('\nEnter your email: ')
}

ID = '''
Name: {} 
Age: {}
Mobile: {}
Email: {}
'''.format(Bio_data['name'], Bio_data['age'], Bio_data['mobile'],Bio_data['email'])

if Bio_data['name'] == '':
    print('\nEntered name is not valid please enter a valid name !')
    exit()
if Bio_data['age'] == '':
    print('\nEntered Age is not valid please enter a valid age !')
    exit()
elif Bio_data['age'] < 18:
    print('\ntoo young to enter, try again in a few years')
    exit()

if ID.__contains__('@gmail.com') == False:
    print('Invalid email address format')
    exit()

if Bio_data['mobile'] == '':
    print('\nEntered mobile number is not valid please enter a valid number !')
    exit()
elif Bio_data['mobile'] > 999999999:
    print('''\n             WELCOME TO MY PYTHON PROJECT\n
 Please wait while your data is being registered...
    ''')
elif Bio_data['mobile'] > 9999999999:
    print('Please enter a valid mobile number')
    exit()
else:
    print('mobile number should have 10 digits')
    exit()

print(ID)