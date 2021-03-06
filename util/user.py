import json
import random
import string
import pyperclip

accounts = "accounts.json"


def login(username, password):
    """ Log in a new user """
    global accounts
    accounts = list_accounts()
    for account in accounts:
        if account['account'] == username and account['password'] == password:
            return True
        else:
            print('Invalid username or password..')


def add_user(account, name, password):
    """
Add new users to the user_list array
"""
    global accounts
    accounts = list_accounts()
    accounts.append({'account': account, 'name': name, 'password': password, '': '\n'})
    _save_user_accounts_(accounts)


def random_pass():
    """ Generate a random password """
    return (''.join(
        random.choice(string.ascii_letters + string.digits + ".',={}[]-/|£$%^&*()_+~#@?><") for _ in range(10)))


def search_account(name):
    """ Search for an account on the json file """
    global accounts
    accounts = list_accounts()
    for account in accounts:
        if account['account'] == name:
            return account


def del_user(name):
    """ Delete a user object from the json file """
    global accounts
    accounts = list_accounts()
    accounts = [account for account in accounts if account['account'] != name]
    _save_user_accounts_(accounts)


def list_accounts():
    with open('accounts.json', 'r') as json_file:
        return json.load(json_file)


def _save_user_accounts_(accounts):
    """ Save all user accounts """
    with open('accounts.json', 'w') as json_file:
        json.dump(accounts, json_file, sort_keys=True, indent=4)
