class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # 用雙底線 "__" 表示私有屬性

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存入 {amount} 元，新餘額為 {self.__balance} 元")
        else:
            print("存款金額必須大於 0")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"取出 {amount} 元，新餘額為 {self.__balance} 元")
        else:
            print("提款金額無效")

    def get_balance(self):
        return self.__balance