''' 1. 建立 class '''

# 類別範例
class Dog:
    def bark(self):
        print("汪汪！")

my_dog = Dog()  # 建立物件
my_dog.bark()   

''' 2. __init__() Function'''
# 建立一個學生類別
class Student:
    def __init__(self, name, age):
        self.name = name  # 實例屬性
        self.age = age

    def introduce(self):   # 方法
        print(f"我是 {self.name}，今年 {self.age} 歲。")

# 建立物件
student1 = Student("小明", 20)
student2 = Student("小華", 22)

# 呼叫方法
student1.introduce()  # 輸出：我是小明，今年 20 歲。
student2.introduce()  # 輸出：我是小華，今年 22 歲。


''' 3. 封裝 (Encapsulation) '''

# 封裝銀行帳戶
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # 私有屬性

    def deposit(self, amount):  # Setter
        if amount > 0:
            self.__balance += amount
            print(f"存入 {amount}，餘額：{self.__balance}")
        else:
            print("存款金額需大於 0")

    def get_balance(self):      # Getter
        return self.__balance

account = BankAccount("小明", 1000)
account.deposit(500)          # 輸出：存入 500，餘額：1500
print(account.get_balance())  # 輸出：1500
# print(account.__balance)    # 會報錯，無法直接存取私有屬性


''' 4. 繼承 (Inheritance) '''

# 動物與狗的繼承
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("我會發出聲音！")

class Dog(Animal):
    def speak(self):           # 方法覆寫
        print(f"{self.name} 說：汪汪！")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} 說：喵喵！")

dog = Dog("小黑")
cat = Cat("小花")
dog.speak() 
cat.speak()


''' 5. 多型 '''
# 統一呼叫不同物件的行為
def make_animal_speak(animal):
    animal.speak()

animals = [Dog("小黑"), Cat("小花")]
for animal in animals:
    make_animal_speak(animal)