class Account:
    def __init__(self, account, balance=0):
        self.__account = account
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def _withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds.")

    @property
    def account(self):
        return self.__account

    @property
    def balance(self):
        return self.__balance

    def display_account_info(self):
        print(f"Account: {self.__account}")
        print(f"Balance: ${self.__balance}")
