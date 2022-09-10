
class iPhone_chahiye:
    def mujhe_iPhone_chahiye():
        user_input = input('what are you studying?: ')
        if user_input == 'python':
            print('iPhone 14 hee milega aapko')
        elif user_input == 'data science':
            print('iPhone 14 pro milega aapko')
        elif user_input == 'ai':
            print('iPhone 14 max milega aapko')
        elif user_input == 'ml':
            print('iPhone 14 pro max milega aapko')
        else:
            print('kuch na milega aapko niklo')

calling = iPhone_chahiye
calling.mujhe_iPhone_chahiye()

user_age = int(input('what is your age: '))
class scooty_trainer_1():
    def __init__(self, age):
        self.age = age
    def learn_scooty(self):
        if self.age <= 12:
            print('can\'t learn scooty yet')
        elif self.age > 12 and self.age < 26:
            print('500 rupiya lagega')
        elif self.age > 26 and self.age < 50:
            print('1000 rupiya lagega')
        elif self.age >50 and self.age <100:
            print('2500 rupiya lagega')

callingTrainer = scooty_trainer_1
callingTrainer(user_age).learn_scooty()

myage = int(input('what is your age: '))
class scootyTrainer2():
    
    def __init__(self,age):
        self.age = age
    
    def scooty(self):
        if self.age <= 12:
            print('can\'t learn scooty yet')
        elif self.age > 12 and self.age < 26:
            return 500
        elif self.age > 26 and self.age < 50:
            return 1000
        elif self.age >50 and self.age <100:
            return 2500
    
    # dictionary me error a rha haiaur ek function ke andar doosra function nahi call ho raha hai
    mydict = {
        'age': myage,
        'money': scooty(myage)
        }
    # print('you are', mydict['age'],'years old and your total amount paid is ', mydict['money'])

    def type_of_scooty(self):
        if self.age > 12 and self.age < 26: #and scooty() == 500:
            print('u get a smol scooty')
        elif self.age > 26 and self.age <50: #and scooty() == 1000:
            print('u get a medium scooty')
        elif self.age > 50 and self.age < 100: #and scooty() == 2500:
            print('u get a supported scooty') 
callingTrainer2 = scootyTrainer2
callingTrainer2(myage).type_of_scooty()


# burger function banaya hai 4 args ke saath without return args toppings judge karengi user input ke saath
#     user input dega list me se joki use provide hogi as he progresses 
#     vegetable me option hai khaali chodne ka
#     last me jaake jo aap le rahe ho wo print kara dega aur function call ho jayega


buns = ['0. parmesan bread' , '1. oregano parmesan bread' , '2. wheat bread' , '3. premium bread']
print('\n', buns)
bunn = int(input('\nwhat kind of bread would you like: ')) 
vegetables = ['0. lettuce' , '1. tomato' , '2. onion' , '3. cucumber' , '4. corn']
print('\n', vegetables)
veggie1 = input('\nchoose your vegetable 1: ')
veggie2 = input('\nchoose your vegetable 2: ')
pattyoption = ['0. aloo tikki', '1. kebab patty', '2. chicken patty']
print('\n',pattyoption)
patty = int(input('\nchoose your patty: '))
saucy = ['0. mayonnaise', '1. jalapeno dip', '2. Cheese']
print('\n', saucy)
sauce = int(input('\nchoose sauce: '))
def burger(bun, veg1, veg2,patt,sauces):
    if bun == 0:
        print('\nbread chosen: ', buns[0])
    elif bun == 1:
        print('\nbread chosen: ', buns[1])
    elif bun == 2:
        print('\nbread chosen: ', buns[2])
    elif bun == 3:
        print('\nbread chosen: ', buns[3])
    else:
        print('\nerror: no such bread')
    if veg1 == '0':
        print('\nveggie1 chosen: ',vegetables[0])
    elif veg1 == '1':
        print('\nveggie1 chosen: ',vegetables[1])
    elif veg1 == '2':
        print('\nveggie1 chosen: ',vegetables[2])
    elif veg1 == '3':
        print('\nveggie1 chosen: ',vegetables[3])
    elif veg1 == '4':
        print('\nveggie1 chosen: ',vegetables[4])
    elif veg1 == '':
        print('\nno veggie selected')
    else:
        print('\ninvalid veggie chosen')
        exit()
    if veg2 == '0':
        print('\nveggie2 chosen: ',vegetables[0])
    elif veg2 == '1':
        print('\nveggie2 chosen: ',vegetables[1])
    elif veg2 =='2':
        print('\nveggie2 chosen: ',vegetables[2])
    elif veg2 == '3':
        print('\nveggie2 chosen: ',vegetables[3])
    elif veg2 == '4':
        print('\nveggie2 chosen: ',vegetables[4])
    elif veg2 == '':
        print('no veggie selected')
    else:
        print('invalid veggie chosen')
        exit()
    if patt == 0:
        print('\npatty chosen:', pattyoption[0])
    elif patt == 1:
        print('\npatty chosen:', pattyoption[1])
    elif patt == 2:
        print('\npatty chosen:', pattyoption[2])
    else:
        print('\ninvalid patty chosen')
        exit()
    if sauces == 0:
        print('\nsauce chosen: ', saucy[0])
    elif sauces == 1:
        print('\nsauce chosen: ', saucy[1])
    elif sauces == 2:
        print('\nsauce chosen: ', saucy[2])
    


print('''
===============================================================================================================
                            THANK YOU FOR WAITING HERE'S WHAT YOU ARE ORDERING
===============================================================================================================
''')
burger(bunn,veggie1,veggie2,patty,sauce)


#function create kara jo ki status check karta hai student ka acc to marks input by user and checks some conditions
#function type without arguments but with return
user_input = input('\n\nmarks scored in test: ')
def status():
    if user_input == '100':
        return 'topped the class'
    elif user_input > '75':
        return 'passed the test'
    else:
        return 'failed the test'
status()

user_name = input('\nenter your name: ')
x = f'''
Dear,{user_name}, you have {status()}
'''
print(x)



