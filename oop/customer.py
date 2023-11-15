from account import Account


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
