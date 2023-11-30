class Account:
#used to initialize account can be used as template for variations in accounts.
    def __init__(self, name, value):
        #initialize the account with a starting value
        self.name = name
        self.value = value

    def add_money(self, value):
        #function to add money to the account
        self.value += value
        return print("{} account now contains {}".format(self.name, self.value))

