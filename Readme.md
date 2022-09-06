# NOTES
## GK
1. created by Guido Van Rossum in 1991 
1. It is an OOP
1. OOPs have 6 basic concepts 
    1. Class
    1. Object
    1. Inheritance
    1. Polymorphism
    1. Abstraction
    1. Encapsulation
1. Function - Jab ek function kisi class ka part nahi hota hai tab wo function hota hai otherwise usko method bolte hai

1. Method - jab koi function kisi class ka part ban jata hai tab usko Method bolte hai
1. Variable - variable ek container jaisa hota hai jo value store karta hai, isme hum saare data types daal sakte hai
    1. Naming a variable -
        1. It cannot start with an integer
        1. It cannot start with a special char(_)
        1. Only special char that is allowed is (_)
        1. Starts with alphabet only
        1. Cannot contain spaces
        1. Name cannot be a pre-defined keyword
    2. Syntax -
        1.  VariableName = 'strings inside apostrophe'
        1. VarName1 = 12    #integers are written without apostrophe
        1. VarName2 = [1,2,3,4,5]  #can store lists, tuples, set, dictionary
1. Data is stored in databases we'll learn about mySQL it stores the ouput from a code
1. we can input data in the form of (numbers, alphabets or special characters) in any programming language

## DATA TYPES

1.  There are 4 data types in python namely - list[], tuple(), set{}, Dictionary{}
1. we can convert one data type into other forms of data types 
like:
    1. list to tuple 
    1. tuple to list
    1. can get items of dict in tuples by using .items()
    1. set to list/tuple
    1. list to set
1. we can also cast numbers and strings:
    1. int to float
    1. float to int
    1. int to complex
    1. float to complex
    1. int to str
    1. float to str

### TUPLE
1. syntax = ('hello', 'hi', 1,2,3,4,5)

1. you can't change data inside tuple with methods 

1. each element inside a tuple is indexed this means you can call an element with its index number

1. you can only count or get index of a value inside the tuple through methods

### LIST
1. syntax = [1,2,3,4,5, 'hello', 'hi']

1. we can change data inside lists using methods syntax.insert(10,11,12) check homework.py for more methods

1. each element inside a list is indexed

### DICTIONARY
1. syntax = {key:value} or <br/>
dict = {<br/>
    'PersonalInfo' = {<br>
    'name': 'Daksh',<br/>
    'age': 18
    }<br>
}
<br>print(dict['PersonalInfo']['age'])<br>
this will print 'age' i.e. 18
1. they are unindexed, as they are stored in pairs
1. data in dictionary is stored in key value pairs

1. various methods in dictionary similar to list
1. to call a specific key in a dictionary:<br/>


### SET
1. syntax = {1,2,3,4,'hi','hello'}
1. elements are unordered, unchangeable(can add or remove items tho...) and unindexed
1. there are some methods in set like union, intersection, issubset, issuperset etc..

## FORMAT METHOD
we currently use format method to input variable value in between a string
there are two forms of the format method respectively
1. f
2. .format( )<br>

example:  
name = 'Daksh'  
age = 18  
x = f '''  
age = {age}  
name = {name}  
'''  
print( x )
### OR
k = '''My name is {n} and I am {a} years old'''.format(n = name, a = age)  
print(k)

## OPERATORS
### ARITHMETIC OPERATORS
1. ' + ' - addition
1. ' - ' - subtraction
1. ' * ' - multiplication
1. / - division
1. % - modulo - tells the remainder - 5%2 = 1
1. ** - power of - 2**2 = 4
1. // - floor division - rounds result down to least whole number - 9//2 = 4
### ASSIGNMENT OPERATORS: 
1. = (assigns value to a variable)
1. += (a += b | a = a + b)
1. -= (a -= b | a = a - b)
1. **= (a **= b | a = a ** b) similarly /, *, %= and //=  
#### THESE HAVE BITWISE FUNCTIONALITY:
<<=  
'>>='  
&=  
|=  
^=  
### COMPARISON OPERATORS
BOOLEAN OPERATORS  
==	 ->   Equal  
!=	 ->   Not equal to  
'>'	 ->   Greater than  
<	 ->   Less than  
'>=' ->  Greater than or equal to  
<=	 ->   Less than or equal to  
### LOGICAL OPERATORS
and - Returns True if both statements are true  
or - Returns True if one of the statements is true  
not - Reverse the result, returns False if the result is true
### IDENTITY OPERATORS
is - Returns True if both variables are the same object  
is not - Returns True if both variables are not the same object
### MEMBERSHIP OPERATORS
in - Returns True if a value is present inside the object  
not in - Returns True if a value is not present inside the object 
### BITWISE OPERATORS
1. & -> and
1. | -> or
1. ~ -> not
1. ^ -> xor
1. << -> fill left with zeroes
1. '>>' -> fill right with zeroes

## CONDITIONS
1. There are three types of conditions: If, else and elif
1. example:

name = 'Daksh'  
if name == 'Daksh':  
&nbsp; &nbsp; &nbsp;&nbsp; print('hello Daksh')  
elif name == 'Sushil':  
&nbsp;&nbsp;&nbsp;&nbsp; print('hello sir')  
else:  
&nbsp;&nbsp;&nbsp;&nbsp; print('hello, unknown user')  
<br>
-------------------------------ALSO-------------------------------
<br/>  
if name == 'Daksh':  
&nbsp;&nbsp;&nbsp;&nbsp; pass  
#pass will not pass the condition without giving an error when we don't want to input a function  
#exit() stops the code right there and exits the code  
## LOOPS
### WHILE LOOPS
parts of while loop
1. initialize/starting point
1. condition check hoti hai
1. work karta hai jo karne ko bolte hai
1. increment karta hai (i ka increment hota hai)

keywords
1. break - finds a number or string and stops the code there
1. continue - finds a number or string and skips that value

#### #NOTE
else statement in while loop is always executed 
 
example:  
i = 1  
while i <= 1000 :  
&nbsp;&nbsp;&nbsp;&nbsp;print(' i = ', i)  
&nbsp;&nbsp;&nbsp;&nbsp;i += 1  
else:  
&nbsp;&nbsp;&nbsp;&nbsp;print( ' yo ' )
