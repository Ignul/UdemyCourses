import requests


class Account:

    def __init__(self, first_name, last_name, balance):

        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def __str__(self):
        return f"{self.first_name} {self.last_name} has {self.balance}$"

    def deposit(self, amount):

        if amount < 0:
            print("Can't deposit negative numbers.")

        else:
            self.balance += amount
            print(f"The amount of: {amount}$ has been added to {self.first_name} {self.last_name} account.")
            print(f"Now the balance is: {self.balance}$")

    def withdraw(self, amount):

        if self.balance < amount:
            print("Insufficient funds.")

        elif amount < 0:
            print("Can't withdraw negative numbers.")

        else:
            self.balance -= amount
            print(f"The amount of: {amount}$ has been withdrawn from {self.first_name} {self.last_name} account.")
            print(f"Now the balance is: {self.balance}$")

    def retrieve_email(self):

        # Imagine having a bank at localhost :D
        response = requests.get(f"http://localhost/bankapi/{self.last_name}/{self.first_name}/email")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
