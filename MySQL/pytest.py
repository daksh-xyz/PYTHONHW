import mysql.connector as mcon
from beautifultable import BeautifulTable
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
#     ID int(8) not null PRIMARY KEY AUTO_INCREMENT,
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

def updatem():    
    #       MY CODE WHICH WAS ADEQUATE BTW                                                                  #function that updates mysql when userinput is 2 
    # field1 = input('\nEnter the field you want to change: ')                        #if elses are used so that if user doesnt input anything returns to main menu instead of giving error
    # if field1 == '':                                                                #else will make the code proceed, if user inputs anything the code will proceed
    #     crudsystem()
    # else:
    #     value1 = input('\nEnter the correct value you want to change to: ')
    # if value1 == '':
    #     crudsystem()
    # else:
    #     field2 = input('\nEnter unique field where incorrect value is there: ')
    # if field2 == '':
    #     crudsystem()
    # else:
    #     value2 = input('\nEnter incorrect value: ')
    # if value2 == '':
    #     crudsystem
    # else:
    #     query = """UPDATE monthly_expenses SET {} = {} WHERE {} = {}""".format(field1, value1 , field2, value2)
    #     crud.execute(query)
    #     db.commit()
    print('''
        --------------------------------------
                SQL MANAGEMENT SYSTEM
        --------------------------------------
        What do you want to update?
        1. NAME
        2. THING
        3. PRICE
        4. EXIT
    ''')
    
    try:
        user_choice = input('\nWhat do you want to UPDATE: ')
    except ValueError:
        print('\nEnter integer value only')
    
    change = input('\nEnter ID number: ')
    if user_choice == '1':
        updatedName = input('\nEnter New Name: \n')
        query = f"UPDATE monthly_expenses SET NAME = '{updatedName}' WHERE ID = {change} "
    elif user_choice == '2':
        updatedThing = input('\nEnter New Thing: \n')
        query = f"UPDATE monthly_expenses SET THINGs = '{updatedThing}' WHERE ID = {change}"
    elif user_choice == '3':
        updatedPrice = input('\nEnter New Price: \n')
        query = f"UPDATE monthly_expenses SET PRICE = {updatedPrice} WHERE ID = {change}"
    elif user_choice == '4':
        print('EXITING PROGRAM...')
    else:
        print('Invalid Input!')
        crudsystem()
    crud.execute(query)
    db.commit()

def deletem():                                                                  # function that deletes row on userinput 3 same logic as above
    change = input('\nEnter ID number: ')
    if change == '':
        crudsystem()
    else:
        query = f"DELETE FROM monthly_expenses WHERE ID = {change}"
        crud.execute(query)
        db.commit()
        

def insertm():
    name = input('\nEnter your Name: ')
    things = input('\nItem bought: ')
    try: 
        price = int(input('\nCost: '))
    except ValueError:
        print('please enter integer values only') 
    query = "INSERT INTO monthly_expenses (NAME, THINGS, PRICE) VALUES (%s, %s, %s)".format(name, things, price)
    val = (name, things, price)
    crud.execute(query, val)
    db.commit()

def readm():
    crud.execute("SELECT * FROM monthly_expenses")
    # For fetching all data form db table use fetchall() method
    all_data = crud.fetchall()
    bt = BeautifulTable()
    # Check lenght of rows
    bt.column_headers = ['Sr.No','ID','NAME','THING','PRICE','DATE']
    i=1
    for row in all_data:
        add_no = list(row)
        add_no.insert(0, i)
        bt.append_row(add_no)
        i+=1
    print(bt)


def crudsystem():
    print('''
        --------------------------------------
                SQL MANAGEMENT SYSTEM
        --------------------------------------
        Do you want to:
        1. Insert data in table
        2. Update a value in table
        3. Delete a row from table
        4. Read current table
        5. Exit                               v0.1
        ''')
    user_input = input('What do you want to do: ')
    if user_input == '1':
        print('INSERTING IN TABLE monthly_expenses')
        insertm()
        readm()
        crudsystem()
    elif user_input == '2':
        print('\nUPDATING TABLE monthly_expenses')
        readm()
        updatem()
        readm()
        crudsystem()
    elif user_input == '3':
        print('\nYOU ARE NOW DELETING A ROW')
        readm()
        deletem()
        readm()
        crudsystem()
    elif user_input == '4':
        print('\nREADING FROM monthly_expenses')
        readm()
        crudsystem()

    elif user_input == '5':
        print('\nEXITING PROGRAM....\n')
    else:
        print('INVALID INPUT, TRY AGAIN!')
        crudsystem()


crudsystem()

# def IDs():
#     crud.execute("SELECT ID FROM monthly_expenses")
#     x = crud.fetchall()
#     for d in x:
#         print(d,)
# IDs()