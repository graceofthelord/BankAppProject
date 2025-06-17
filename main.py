import streamlit as st
st.set_page_config(page_title='BANK APP', layout='centered')

class Account:
    def _init_(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print (self.balance)

    def deposit(self, amount):
        self.balance += amount
from account import Account


class CurrentAccount(Account):
    def _init_(self, balance):
        Account._init_(self, balance)

    def withdraw(self, amount):
        super().withdraw(amount)

from account import Account


class SavingsAccount(Account):
    def _init_(self, balance, ):
        Account._init_(self, balance)

    def withdraw(self, amount):
        if amount <= 10000:
            return super().withdraw(amount)
        else:
            print('you have exceeded your limit')

    def deposit(self, amount):
        return super().deposit(amount)

#
