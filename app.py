from util import user

User_Choice = """
Enter:  
    - '1' to create a random password
    - '2' to add a new account
    - '3' to check for a user
    - '4' to delete an account
    - 'q' quit the application
Your choice: """


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
            delete_account()
        else:
            print('Unknown command')
        print('')
        user_input = input(User_Choice).lower()
    print('')
    print('...Exiting the program')


def create_random_pass():
    pass


def create_new_account():
    account = input('Enter the account name: ')
    name = input("Enter your Username: ")
    password = input('Enter the password: ')
    user.add_user(account, name, password)


def find_accounts():
    user_to_find = input('Enter the name you want to search for: ')


def delete_account():
    acc_name = input('Enter the name of the account to delete: ')
    user.del_user(acc_name)


menu()
