
import shelve

class Account:
#used to initialize account can be used as template for variations in accounts.
    def __init__(self, name, value = 0):


        #initialize the account with a starting value
        self.name = name
        self.value = value




class Debt(Account):

    def __init__(self, name, value=0, intrest_rate = 0):
        super().__init__(name, value)
        self.intest_rate = intrest_rate

class Asset(Account):

    def __init__(self, name, value = 0, intrest_rate = 0):
        super().__init__(name, value)
        self.intrest_rate = intrest_rate












'''def main():
    creating = True
    while creating == True:
        current_account = input("What account would you like to create?")
        current_value = input("What is the value of this account?")
        current_account = Account(current_account, current_value)
        current_account.update()

        check = input('Would you like to create another account? Y/N')
        if check.upper == 'Y':
            continue
        else:
            creating = False


if __name__ == '__main__':
    main()
'''







