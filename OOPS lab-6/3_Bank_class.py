class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        if(amount>0):
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if (0 < amount <= self.balance):
            self.balance-= amount
            print(f"Withdrew {amount}, New balance is {self.balance}.")
        elif( amount > self.balance):
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
        
        def check_balance(self):
            print(f"The current balance is {self.balance}.")

account = BankAccount("Alice", 1000)

account.check_balance()
account.deposit(500)
account.withdraw(200)
account.check_balance()