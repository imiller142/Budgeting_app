#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

import pickle

from Account import Account as a

with open('accounts.bin', 'rb') as f:
    accounts = pickle.load(f)

box_values = [key for key,val in accounts.items()]

class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.frame1 = ttk.Frame(master)
        self.frame1.configure(height=200, width=200)
        combobox1 = ttk.Combobox(self.frame1, values= box_values)
        combobox1.pack(side="top")
        self.account_value = tk.Message(self.frame1)
        self.account_value.pack(side="top")
        self.frame1.pack(side="top")
        combobox1.bind('<<ComboboxSelected>>', self.on_select)
        add_money = ttk.Entry(self.frame1)
        add_money.pack(side="top")
        add_money_confirm = ttk.Button(self.frame1)
        add_money_confirm.pack(side="top")


        # Main widget
        self.mainwindow = self.frame1

    def on_select(self, event):
        print(event)
        selected = event.widget.get()
        self.account_value['text'] = accounts[selected].value
    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()
