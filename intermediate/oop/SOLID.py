"""1. Single Responsibility Principle 單一職責原則"""


# bad
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_db(self):
        print(f"Saving {self.name} to db")

    def send_email(self):
        print(f"Sending email to {self.email}")


"""SRP"""


# Data class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# processing to db
class UserRepo:
    def save_to_db(self, user):
        print(f"Saving {user.name} to db")


# processing to email
class EmailService:
    def send_email(self, user):
        print(f"Sending email to {user  .email}")
