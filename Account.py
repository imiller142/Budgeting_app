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

    def pickle(self):
        with open(('C:\\Users\\ismiller\\Documents\\Coding\\Python\\Budgeting_app\\pickles' + '\\' + self.name + '.pickle'), 'wb') as f:
            pickle.dump(self, f)


    def add_money(self, value):
        #function to add money to the account
        self.value += value

        print("{} account now contains {}".format(self.name, self.value))
            #create an intial account with a value defaulting to 0

def main():

    savings = Account('Savings', 1200)
    checking = Account('Checking', 10)

    savings.pickle()


if __name__ == '__main__':
    main()








