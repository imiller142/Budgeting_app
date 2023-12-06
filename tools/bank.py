import shelve
import tools.account as account

class Bank:

    def __init__(self):
        with shelve.open('data\\accountsDB') as db:
            self.data = dict(db)



    def create_account(self):
        account_name = input("what is the name of the account are you creating?")
        account_value = input("What is the value of this account?")
        account_type = input("what type of account is this Debt or Asset? d/a")

        if account_type == 'd':
            intrest_rate = input("what is the intrest rate on this account?")
            account_name = account.Debt(account_name, account_value, intrest_rate)
        else:
            account_name = account.Asset(account_name, account_value)
        self.store(account_name)


    def quick_create(self, name, value):

        acct = account.Account(name, value)
        return acct

    def store(self,obj):
        with shelve.open('data\\accountsDB') as db:
            db[obj.name] = obj



    def list_accounts(self):


            for key,val in self.data.items():
                print(key, val.value)

