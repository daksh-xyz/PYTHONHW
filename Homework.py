from audioop import reverse
from ctypes import addressof
from re import X
from typing import Reversible


intNum = 73
floatNum = 73.73
complexNum = 73j
print(floatNum, ' => ', int(floatNum))
print(intNum, '=>', float(intNum))
print(intNum, '=>', complex(intNum))
print(floatNum, '=>', complex(floatNum))
#all of the print functions have 3 arguments 0 is a variable, 1 is a string,2 is a class viz a converter
#                                                            OR
#int() converts float to integer value 
#float() converts integer to float value(decimal point value)
#complex() converts integer or float value to complex value, imaginary part is j which does not have a def value
numValues = f'''
intNum = {intNum} => {int(floatNum)}  
floatNum = {floatNum} => {float(intNum)}
complexNum = {complexNum} => {complex(intNum)} => {complex(floatNum)}

'''
print(numValues)

#data tank 
Name = 'Daksh Lal'
Age = 18                                                                                                           
Mobile = 8287086661                                                                                                
Email = 'dakshuklal@gmail.com'                                                                           
Address = '10/15 Old Rajinder Nagar New Delhi India'
School = 'Bal Bharati Public School'
College = 'MUJ 26'   

#f is short form for format it allows us to introduce variables in our multiline string, variables are called inside{} 
result = f'''
Name = {Name}    
Age = {Age}      
Mobile = {Mobile}
Email = {Email} 
Address = {Address}
College = {College}
'''
print(result)

#20-Aug-22
name = 'Daksh'
Name = 'daksh lal'
print('capitalize:', name.capitalize())
print('upper_case_eve:', name.upper())
print('lower_case_eve:', name.lower())
print('count:', name.count('a'))
print('find_letter:',name.find("k"))
print('tells if string ends with input:', name.endswith("l"))
print('index/position:', name.index("a"))   #prints the position of the letter inside "" when it was used for the first time
print(name.isalnum())
print(name.isalpha())
print(name.isdecimal())
print(name.isdigit())   #true if all are digits
print(name.islower())   #true if all chars are lowercase
print(name.isprintable())
print(name.replace("Daksh","Jatin")) #replaces specified value with another value given after a comma, add an int without'' to specify how many times to replace the word
print(name.rsplit("a")) #splits at a given letter(deletes it too?), annd returns w a list
print(Name.swapcase()) #swaps upper and lower cases duh
print(Name.title())   #first char of each word in caps
print(name.zfill(7))  #adds 0s to the beginning of the string until its length is as specified in the brackets
print('\nLength:', len(name),'\n')  #prints the length of the variable in the bracket no '' reqd
print('\n 1st char of variable(name): ', name[0], '\n')  #prints the first letter of the given word, requires [] brackets
print('\n 0 to 4th char of variable(name): ', Name[0:5], '\n') #x:y, : adds range to print function to print from x till y-1, starts from 0
print('\n 0 to 4th char of variable (name):', name[:5], '\n')  #if we dont put anything in 'x' it meas from start and if 'y' is empty it means for the length of the string  
#NEGATIVE SLICING
print('\n negative slicing:', Name[-3:-1], '\n')

#21-Aug-22
name = 'Daksh'
age = 18
address = 'New Delhi'
course = 'Python'
school = 'BBPSGR'

message = 'Hello Mr. ' + name + ', how are you?' + f''', {age}''' + ' ' + course
print(message)

Bio_data = '''\nHello, my name is {x}\nI am {y} years old\nI currently live in {a}\nI am learning {c}\nI study in {s}'''.format(x=name,y=18,a=address,c=course,s=school)
print(Bio_data)

#tuple => 2 methods only
x = (1,2,3,4,5)
#list => 11 methods
y = ['a','b','c','d','e']
z = [10,11,52,73] #for extend func
z1 = [21,37,65,45] # for funcs ahead of clear
print(x.count(2))     #tells how many times a value has been repeated
print(x.index(4))     #prints out index number of the given int/string
print(y.index('b'))   #same
print(y.count('c'))   #same as x.count
y.append("5")
print(y)              #need to pritn seperately :'(
y.clear()
print(y)
z1.extend(z)
print(z1)
g = z1.copy()
print(g)
z1.insert(3,55)
print(z1)
z.pop(2)
print(z)  #removes 52 can't print in one line prints the removed element
z.remove(10)   
print(z)
z.reverse()  #reverses the list order
print(z)
z1.sort()   #arranges in asc or desc order
#z1.reverse()       makes the above sort intp descending, sorted in ascending order of alpha if there are alphas, if int then inc number wisse
print(z1)