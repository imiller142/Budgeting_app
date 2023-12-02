#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import shelve


import tools.account as account
import tools.account_load as load
import account_functions as func



class NewprojectApp:
    def __init__(self, master=None):
        data_load = load.load_accounts()
        self.box_values = list(data_load.keys())
        print(self.box_values)
        # build ui
        self.frame1 = ttk.Frame(master)
        self.frame1.configure(height=200, width=200)
        combobox1 = ttk.Combobox(self.frame1, values= self.box_values)
        combobox1.pack(side="top")
        self.account_value = tk.Message(self.frame1)
        self.account_value.pack(side="top")
        self.frame1.pack(side="top")

        self.add_account = ttk.Entry(self.frame1)
        self.add_account.pack(side="top")
        self.add_money = ttk.Entry(self.frame1)
        self.add_money.pack(side="top")
        self.add_money_confirm = ttk.Button(self.frame1, command = self.create())
        self.add_money_confirm.pack(side="top")


        # Main widget
        self.mainwindow = self.frame1

     

    def run(self):
        self.mainwindow.mainloop()

    def create(self):
        name = self.add_account.get()
        value = self.add_money.get()

        new = func.quick_create(name, value)
        func.store(new)

if __name__ == "__main__":
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()
