import random
import string

user_list = 'accounts.csv'


def create_account_table():
    with open(user_list, 'w'):
        pass


def login(username, password):
    """ Log in a new user """
    pass


def random_pass():
    return ''.join(
        random.choice(string.ascii_letters + string.digits + ".',={}[]-/|\£$%^&*()_+~#@?><") for _ in range(10))


def add_user(account, name, password, ):
    """
    Add new users to the user_list array
    """
    with open(user_list, 'a') as csv_file:
        csv_file.write(f'{account}, {name}, {password} \n')


def list_accounts():
    with open(user_list, 'r') as csv_file:
        lines = [lines.strip().split(',') for lines in csv_file.readlines()]
    return [
        {'Account': line[0], 'Username': line[1], 'Password': line[2]}
        for line in lines
    ]


def _save_user_accounts(users):
    """ Save all user accounts """
    with open(user_list, 'w') as csv_file:
        for user in users:
            csv_file.write(f"{user['Account']}, {user['Username']}, {user['Password']} \n")


def del_user(name):
    """Delete a user"""
    user_accounts = list_accounts()
    for user_account in user_accounts:
        if user_account['Account'] != name:
            _save_user_accounts(user_accounts)

# @classmethod
# def check_user(cls, username):
#     """Check if a user exists"""
