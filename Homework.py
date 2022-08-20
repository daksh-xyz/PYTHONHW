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