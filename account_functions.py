import shelve
import tools.account as account

def create_account():
    account_name = input("what is the name of the account are you creating?")
    account_value = input("What is the value of this account?")
    account_type = input("what type of account is this Debt or Asset? d/a")

    if account_type == 'd':
        intrest_rate = input("what is the intrest rate on this account?")
        account_name = account.Debt(account_name, account_value, intrest_rate)
    else:
        account_name = account.Asset(account_name, account_value)
    return account_name


def quick_create(name, value):

    acct = account.Account(name, value)
    return acct

def store(obj):
    with shelve.open('data\\accountsDB') as db:
        db[obj.name] = obj



def list_accounts():

    with shelve.open('data\\accountsDB') as db:
        print('Current accounts are \n')
        for key,val in db.items():
            print(key, val.value)
            
