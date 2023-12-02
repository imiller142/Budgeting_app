
import shelve

def load_accounts():

    with shelve.open('data\\accountsDB') as db:
        data = dict(db)
    return data

