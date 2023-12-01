import os.path
import json
import pickle

import os

here = os.path.dirname(os.path.abspath(__file__))
class Account:
#used to initialize account can be used as template for variations in accounts.
    def __init__(self, name, value = 0):


        #initialize the account with a starting value
        self.name = name
        self.value = value



    def add_money(self, value):
        #function to add money to the account
        self.value += value

        print("{} account now contains {}".format(self.name, self.value))
        return self.value
            #create an intial account with a value defaulting to 0


savings = Account('Savings', 1200)
checking = Account('Checking', 10)

accounts = [savings, checking]

accounts_pickle = {}

for item in accounts:
    accounts_pickle[item.name] = item


with open(os.path.join(here,'accounts.bin'), 'wb') as f:
    pickle.dump(accounts_pickle, f)






