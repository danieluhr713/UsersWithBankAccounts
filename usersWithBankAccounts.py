class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account1 = BankAccount(int_rate = 0.02, balance=100)
        self.account2 = BankAccount(int_rate=0.04, balance = 200)


class BankAccount:
    def __init__(self, int_rate = 0.0345, balance = 100.0):
        self.rate = int_rate
        self.acctBalance = balance

    def deposit(self, amount):
        self.acctBalance += amount
    
    def withdraw(self, amount):
        self.acctBalance -= amount

    def display_account_info(self):
        print("Balance: ", self.acctBalance)


Daniel = User('Daniel', 'danuhr713@gmail.com')
print(Daniel.name)
Daniel.account1.deposit(150)
Daniel.account1.withdraw(100)
Daniel.account1.display_account_info()
Daniel.account2.deposit(400)
Daniel.account2.withdraw(50)
Daniel.account2.display_account_info()

