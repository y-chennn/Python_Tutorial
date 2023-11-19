class Account:
    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder
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

    @property
    def account(self):
        return self.__account_holder

    @property
    def balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Balance for {self.account_holder}: ${self.balance}")


class Customer:
    def __init__(self, name) -> None:
        self.__name = name
        self.account = []

    def set_account(self, account):
        self.account.append(account)

    def display_customer_info(self):
        print(f"Customer: {self.__name}")
        for acc in self.account:
            print(f"Account: {acc.account}, Balance: {acc.balance}")


if __name__ == "__main__":
    c = Customer("123")
    a = Account("123", 0)
    c.set_account(a)
    c.display_customer_info()
