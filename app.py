import pyfiglet
import pyperclip
from termcolor import cprint

from util import credentials
from util import user

banner = cprint(pyfiglet.figlet_format('.    PassLocker    .'), 'yellow')

welcome = f""" 
 
***********************************************************
*                                                         *
*                Vick's Password Locker:                  *
*                                                         *
***********************************************************
\n
User Menu:  
    - 1: Login
    - 2: Create a new account
    - q: quit the application \n
Choose an option:

 """


def welcome_func():
    input_choice = input(welcome)
    while input_choice != 'q':
        if input_choice == '1':
            login()
        elif input_choice == '2':
            menu()
        else:
            print('Invalid input..')
        print('')
        input_choice = input(welcome)
    print(f'You choose option {input_choice}')
    print('..bye bye')


User_Choice = f"""  
***********************************************************
*                                                         *
*              Create a new user Account:                 *
*                                                         *
***********************************************************
\n
New account user menu:  
    - 1: to create a random password
    - 2: to add a new account
    - 3: to search for an account
    - 4: to list all available accounts
    - 5: to delete an account
    - q: quit the application \n
Your choice:

 """


def menu():
    user_input = input(User_Choice).lower()

    while user_input != 'q':
        if user_input == '1':
            create_random_pass()
        elif user_input == '2':
            create_new_account()
        elif user_input == '3':
            find_accounts()
        elif user_input == '4':
            list_accounts()
        elif user_input == '5':
            delete_account()
        else:
            print('Unknown command')
        print('')
        user_input = input(User_Choice).lower()
    print('')
    print('...Your passwords are safe now!....exiting')


def login():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    # user.login(username, password)
    credentials.login(username, password)


def create_random_pass():
    print(user.random_pass())
    pyperclip.paste()


def create_new_account():
    account = input('Enter the account name: ')
    name = input("Enter your Username: ")
    password = input('Enter the password: ')
    user.add_user(account, name, password)
    print('')
    print(f'Hello {name}, your account has been created successfully.')


def list_accounts():
    user.list_accounts()
    print('')
    for accounts in user.list_accounts():
        print(accounts)


def find_accounts():
    user_to_find = input('Enter the name you want to search for: ')
    user.search_account(user_to_find)
    print(user.search_account(user_to_find))


def delete_account():
    acc_name = input('Enter the name of the account to delete: ')
    user.del_user(acc_name)


if __name__ == '__main__':
    welcome_func()
