intNum = 73
floatNum = 73.73
complexNum = 73j
print(floatNum, ' => ', int(floatNum))
print(intNum, '=>', float(intNum))
print(intNum, '=>', complex(intNum))
print(floatNum, '=>', complex(floatNum))

#                                                            OR
numValues = f'''
intNum = {intNum}
floatNum = {floatNum}
complexNum = {complexNum}
'''
print(floatNum, ' => ', int(floatNum))
print(intNum, '=>', float(intNum))
print(intNum, '=>', complex(intNum))
print(floatNum, '=>', complex(floatNum))



print('''
|-----------------------------------------------------------------------------------------------------------------------------|
|                                                              BIODATA                                                        |
|-----------------------------------------------------------------------------------------------------------------------------|
|Name: Daksh Lal                                                                                                              |
|Age: 18                                                                                                                      |
|Mobile: 8287086661                                                                                                           |
|Email: dakshuklal@gmail.com                                                                                                  |
|Address: 10/15 Old Rajinder Nagar New Delhi India                                                                            |
|School: Bal Bharati Public School                                                                                            |
|College: MUJ '26                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------|
''')