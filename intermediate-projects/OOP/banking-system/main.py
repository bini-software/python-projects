from bank_account import BankAccount

print("Welcome to Banking System\nFirst create a bank account.\n")

account_no = input("Enter your account number: ")
owner = input("Enter account owner name: ").title()

while True:
    try:
        balance = float(input("Enter starting balance (ETB): "))
        if balance < 0:
            raise ValueError("You must enter positive balance")
        break

    except Exception as e:
        print(f"Error: {e}")
    
account = BankAccount(account_no, owner, balance)

print("\nAccount created successfully.")
print(f"Account Number : {account_no}")
print(f"Owner : {owner}")
print(f"Starting Balance : (ETB) {balance}")

while True:
    print("""
          \nBanking Menu:
          1. Deposit
          2. Withdrawal
          3. Check Balance
          4. Transaction History
          5. Exit
""")
    
    choice = input("Choose an option (1-5): ").lower()
    match choice:

        case "1" | "deposit":
            amount = input("Enter deposit amount: ")
            message = account.deposit(amount)
            if message:
                print(message)

        case "2" | "withdrawal":
            amount = input("Enter withdrawal amount: ")
            message = account.withdrawal(amount)
            if message:
                print(message)
            
        case "3" | "check balance":
            message = account.check_balance()
            print(message)

        case "4" | "transaction history":
            transactions = account.show_transaction()
            if transactions:
                print("Transaction History")
                for tran in transactions:
                    print(f"\n{tran}")

            else:
                print("There is no any transaction")
            
        case "5" | "exit":
            print("Thank you for using our banking system")
            print("Exiting... Goodbye")
            break

        case "_":
            print("Invalid choice. Try again")