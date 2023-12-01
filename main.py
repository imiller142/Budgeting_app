import pickle

from Account import Account as a

with open('accounts.bin', 'rb') as f:
    accounts = pickle.load(f)


