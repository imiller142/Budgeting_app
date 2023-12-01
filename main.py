import pickle

from Account import Account

with open('pickles\Savings.pickle', 'rb') as f:
    Savings = pickle.load(f)


Savings.add_money(20)

Savings.pickle()



