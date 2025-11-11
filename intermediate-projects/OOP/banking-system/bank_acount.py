from datetime import datetime

class BankAccount:
    def __init__(self, account_no, owner, balance = 0.0):
        self.account_no = account_no
        self.owner = owner.title()
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must greater than 0")
            
            self.balance += amount
            self.transaction.append(f"[{datetime.now()}] Deposit: ETB {amount}. Balance: ETB {self.balance}")
            print(f"Withdrawal successful. Amount: ETB {amount}. Available balance: ETB {self.balance}")

        except Exception as e:
            print(f"Error: {e}")

    def withdrawal(self, amount):   
        try:
            amount = float(amount)
            if amount > self.balance:
                raise ValueError("Insufficiennt balance")
            
            self.balance - amount
            self.transaction.append(f"[{datetime.now()}] Withdrawal: ETB {amount}. Balance: ETB {self.balance}")
            print(f"Withdrawal successful. Amount: ETB {amount}. Available balance: ETB {self.balance}")
            
        except Exception as e:
            print(f"Error: {e}")

    def check_balance(self):
        print(f"Your current balance: ETB {self.balance}")

    def transaction(self):
        for trans in self.transactions:
            print(trans)