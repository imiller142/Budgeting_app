import tools.account as account
import tools.account_load as load
import account_functions as func
import shelve

data = func.create_account()

func.store(data)







print(dict(load.load_accounts()))