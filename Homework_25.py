#DISCARD prints 'a' without 1

# Q1 differences

#                                           difference between discard remove and pop 

# remove gives an error if the element does not exist in the given set whereas discard doesn't do anything
#pop removes a random argument from the given set

#                                    difference between POP REMOVE AND POPITEM in list/set and dict

#       POP
# in lists pop removes the last element or elt at specified index
# in set pop removes a random argument
# in dict pop removes the specified key value pairs (if default given then return that otherwise raises errror)

#       REMOVE
# in lists remove method removes only the first occurrence of a value
# in set remove method removes all instances of an element
# in dict remove method DNE

#       POPITEM
# in lists popitem DNE
# in set popitem DNE
#in dict popitem removes last element and doesnt take any args

# Q2 addition

num_1 = float(input('\nEnter first number: '))                          #float is used to cast input to float
num_2 = float(input('\nEnter second number: '))
s = (num_1) + (num_2)
print(s)
#                                                               OR
# print(add(num_1,num_2))


# if num_1.isdigit() == True and num_2.isdigit() == True:
    # print(s)1
# else:
    # print('error input must be an integer')

#               if we don't use int class then we can use this but without int we can't add these two inputs

# Q3 odd/even
x = input('enter a number: ')
rem = int(x) % 2                        #int is used to cast x string to integer
if rem == 1:
    print('entered number is odd')
elif rem == 0:
    print('entered number is even')
#DISCARD prints 'a' without 1

# Q1 differences

#                                           difference between discard remove and pop 

# remove gives an error if the element does not exist in the given set whereas discard doesn't do anything
#pop removes a random argument from the given set

#                                    difference between POP REMOVE AND POPITEM in list/set and dict

#       POP
# in lists pop removes the last element or elt at specified index
# in set pop removes a random argument
# in dict pop removes the specified key value pairs (if default given then return that otherwise raises errror)

#       REMOVE
# in lists remove method removes only the first occurrence of a value
# in set remove method removes all instances of an element
# in dict remove method DNE

#       POPITEM
# in lists popitem DNE
# in set popitem DNE
#in dict popitem removes last element and doesnt take any args

# Q2 addition
num_1 = float(input('\nEnter first number: '))                          #float is used to cast input to float
num_2 = float(input('\nEnter second number: '))
s = (num_1) + (num_2)
print(s)
#                                                               OR
# print(add(num_1,num_2))


# if num_1.isdigit() == True and num_2.isdigit() == True:
    # print(s)1
# else:
    # print('error input must be an integer')

#               if we don't use int class then we can use this but without int we can't add these two inputs

# Q3 odd/even
x = input('enter a number: ')
rem = int(x) % 2                        #int is used to cast x string to integer
if rem == 1:
    print('entered number is odd')
elif rem == 0:
    print('entered number is even')