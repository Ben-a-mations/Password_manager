import time
import os
import sqlite3
from os.path import exists


conn = sqlite3.connect("data.db")
cursor = conn.cursor()



def main():
    os.system('clear')

    print("-----------------------------------------------------")
    print("---------------SECURE-PASSWORD-MANAGER---------------")
    print("-----------------------------------------------------")
    print("")
    print("Type 'help' for a list of commands")

    a = input(":>> ")
    if a == "help":
        help_menu()
    elif a == "q":
        print("Bye!!")
        time.sleep(1.5)
        exit()
    elif a == "new_pass":
        new_pass()
    elif a == "s_data":
        s_data()
    elif a == "l_pass":
        l_pass()
    elif a == "rem_pass":
        rem_pass()
    else:
        print("Command not found")
        time.sleep(1.5)
        main()


def s_data():
    os.system('clear')
    print('--------------------------------------------')
    print('IF YOU HAVE A CURRENT TABLE AND DONT WANT ')
    print("THE DATA REMOVED PLESE TYPE 'back' TO LEAVE")
    print("IF YOU WANT TO CONTINUE AND MAKE A NEW TABLE")
    print("THAN PLEASE TYPE 'continue'")
    print('--------------------------------------------')

    a = input(':>> ')
    if a == "back":
        main()
    elif a == "continue":
        cursor.execute("CREATE TABLE data (Website TEXT, Username TEXT, Password TEXT, id INTEGER)")
        time.sleep(2)
        print('Done!')
        time.sleep(1.5)
        main()
    else:
        print("Command not found")
        time.sleep(1)
        s_data

def help_menu():
    os.system('clear')
    print('-------------------------------------------------------------------')
    print('l_pass - list of passwords stored')
    print('new_pass - Make a new password | rem_pass - remove a password')
    print('s_data - set up new data table | q - quit')
    print('-------------------------------------------------------------------')
    print("type 'back' to go back to main")

    b = input(':>> ')
    if b == "back":
        main()
    else:
        print("Command not found")
        time.sleep(1.5)
        help_menu()()

def rem_pass():
    os.system('clear')
    print("----------------------------------------------------")
    print("What do you want to delete?")
    rows = cursor.execute("SELECT Website, Username, Password, id FROM data").fetchall()
    print(rows)
    print('')
    print('Please select based on the id number')
    
    a = input(":>> ")
    cursor.execute(f"DELETE FROM data WHERE id = {a}")
    conn.commit()
    print("Done!")
    time.sleep(1.5)
    main()
    



def new_pass():
    os.system('clear')
    print('------------------------------------------------')
    print('Please type the website that the password is on:')
    c = input(":>> ")
    print('Please type the email/username:')
    cc = input(":>> ")
    print('Please type the password you want to set:')
    ccc = input(':>> ')
    print('Please type a new id number you have not used before, note')
    print('if you do, than replacing the password will delete the other')
    print('passwords associated with that id number')
    print('')
    cccc = input(':>> ')

    cursor.execute(f"INSERT INTO data VALUES ('{c}', '{cc}', '{ccc}', '{cccc}')")
    conn.commit()
    print('Done!')
    time.sleep(1.5)

    main()

def l_pass():
    os.system('clear')
    print('-------------------------------------')
    print('List of Stored Passwords:')

    rows = cursor.execute("SELECT Website, Username, Password FROM data").fetchall()
    print(rows)
    print("Type 'back' when done")
    a = input(':>> ')
    if a == 'back':
        main()
    else:
        print("Command not found")
        time.sleep(1)
        l_pass()


main()