intNum = 73
floatNum = 73.73
complexNum = 73j
print(floatNum, ' => ', int(floatNum))
print(intNum, '=>', float(intNum))
print(intNum, '=>', complex(intNum))
print(floatNum, '=>', complex(floatNum))

#                                                            OR
#
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