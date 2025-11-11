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
            self.transactions.append(f"[{datetime.now()}] Deposit: ETB {amount}. Balance: ETB {self.balance}")
            return f"Deposit successful. Amount: ETB {amount}. Available balance: ETB {self.balance}"

        except Exception as e:
            return f"Error: {e}"

    def withdrawal(self, amount):   
        try:
            amount = float(amount)
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            
            self.balance -= amount
            self.transactions.append(f"[{datetime.now()}] Withdrawal: ETB {amount}. Balance: ETB {self.balance}")
            return f"Withdrawal successful. Amount: ETB {amount}. Available balance: ETB {self.balance}"
            
        except Exception as e:
            return f"Error: {e}"

    def check_balance(self):
        return f"Your current balance: ETB {self.balance}"

    def show_transaction(self):
        return self.transactions