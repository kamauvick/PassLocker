import json


def list_accounts():
    with open('accounts.json', 'r') as json_file:
        return json.load(json_file)


def login(username, password):

    """ Log in a new user """
    accounts = list_accounts()
    for account in accounts:
        if account['account'] == username and account['password'] == password:
            return True
        else:
            print('Invalid username or password..')


class credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password
