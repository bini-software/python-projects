#Login System
for i in range(3, 0, -1):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "1234":
        print("Login successful!")
        break    
    elif username != "admin" or password != "1234":
        print("Incorrect username or password.")
        print(f"You have only {i - 1} attempts left!\n")
else:
    print("Access blocked!") 