class Account:
    def __init__(self, holder: str, balance: int = 0):
        self.__holder = holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Balance for {self.__holder}: ${self.__balance}")

    def bet(self, amount: int):
        if self.__balance != 0 and amount >= 0:
            self.__balance -= amount

    @property
    def account(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance
