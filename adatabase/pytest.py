import mysql.connector as mcon
db = mcon.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pytest"
    )


crud = db.cursor()
# query = "CREATE DATABASE pytest"          created a database pytest ggs
# crud.execute(query)

# query = """CREATE TABLE monthly_expenses(
#     ID int(8) not null PRIMARY KEY,
#     NAME varchar(25),
#     THINGS varchar(500),
#     PRICE int(6),
#     DATE timestamp)"""
# crud.execute(query)               #creating a table with fields like id name things price and date

# query = "INSERT INTO monthly_expenses (name, things , price) VALUES (%s, %s, %s)"
# val = ("daksh", "pizza", "499")
# crud.execute(query, val)                                                                  #adding data to table
# db.commit()
# exit()

def updatem():                                                                      #function that updates mysql when userinput is 2 
    field1 = input('\nEnter the field you want to change: ')                        #if elses are used so that if user doesnt input anything returns to main menu instead of giving error
    if field1 == '':                                                                #else will make the code proceed, if user inputs anything the code will proceed
        crudsystem()
    else:
        value1 = input('\nEnter the correct value you want to change to: ')
    if value1 == '':
        crudsystem()
    else:
        field2 = input('\nEnter unique field where incorrect value is there: ')
    if field2 == '':
        crudsystem()
    else:
        value2 = input('\nEnter incorrect value: ')
    if value2 == '':
        crudsystem
    else:
        query = """UPDATE monthly_expenses SET {} = {} WHERE {} = {}""".format(field1, value1 , field2, value2)
        crud.execute(query)
        db.commit()

def deletem():                                                                  # function that deletes row on userinput 3 same logic as above
    field = input('\nEnter the field from which you want to delete: ')
    if field == '':
        crudsystem()
    else:
        value = input('\nEnter a unique value in the chosen field: ')
    if value == '':
        crudsystem()
    else:
        query = "DELETE FROM monthly_expenses WHERE {} = {}".format(field, value)
        crud.execute(query)
        db.commit()

def insertm():
    name = input('\nEnter your name: ')
    things = input('\nItem bought: ')
    try: 
        price = int(input('\nCost: '))
    except ValueError:
        print('please enter integer values only') 
    query = "INSERT INTO monthly_expenses (NAME, THINGS, PRICE) VALUES (%s, %s, %s)".format(name, things, price)
    val = (name, things, price)
    crud.execute(query, val)
    db.commit()

def crudsystem():
    print('''
        --------------------------------------
                SQL MANAGEMENT SYSTEM
        --------------------------------------
        Do you want to:
        1. insert data in table
        2. update a value in table
        3. delete a row from table
        4. exit                               v0.1
        ''')
    user_input = input('What do you want to do: ')
    if user_input == '1':
        print('INSERTING IN TABLE monthly_expenses')
        insertm()
        crud.execute("SELECT * FROM monthly_expenses")
        print(' ID | NAME | THING | PRICE | DATE ')
        z = crud.fetchall()
        for d in z:
            print('\n', d)
        crudsystem()
    elif user_input == '2':
        print('\nUPDATING TABLE monthly_expenses')
        crud.execute("SELECT * FROM monthly_expenses")
        print(' ID | NAME | THING | PRICE | DATE ')
        z = crud.fetchall()
        for d in z:
            print('\n', d)
        updatem()
        crud.execute("SELECT * FROM monthly_expenses")
        print(' ID | NAME | THING | PRICE | DATE ')
        z = crud.fetchall()
        for d in z:
            print('\n', d)
        crudsystem()
    elif user_input == '3':
        print('\nYOU ARE NOW DELETING A ROW')
        crud.execute("SELECT * FROM monthly_expenses")
        print('ID | NAME | THING | PRICE | DATE ')
        z = crud.fetchall()
        for d in z:
            print('\n', d)
        deletem()
        crud.execute("SELECT * FROM monthly_expenses")
        print(' ID | NAME | THING | PRICE | DATE ')
        z = crud.fetchall()
        for d in z:
            print('\n', d)
        crudsystem()
    elif user_input == '4':
        print('\nEXITING PROGRAM....')
    else:
        print('INVALID INPUT, TRY AGAIN!')
        crudsystem()


crudsystem()

def IDs():
    crud.execute("SELECT ID FROM monthly_expenses")
    x = crud.fetchall()
    for d in x:
        print(d,)
IDs()