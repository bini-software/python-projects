#Phone_book App

contacts = {}

while True:
    action = input("Enter your actiion(add, search, Show all, delete, exit): ").lower()
    if action == "add": 
       name = input("Enter name: ").lower()
       phone = input("Enter phone: ") 
       if name in contacts:
           accept = input("The contact is already saved. How can I help you(overwrite / cancel): ").lower()
           if accept == "overwrite":
            contacts[name] = phone 
            print("Contact Saved.")
           elif accept == "cancel":
               print("You canceled.")   
           else:
               print("Invalid character, try again")
       else:
           contacts[name] = phone
           print("Contact Saved.")
                   
    elif action == "search":
        search = input("Enter the name, you looking for their phone: ").lower()
        if search in contacts:
            phone = contacts[search]
            print(f"{search.title()}'s phone number is {phone}")
        else:
            print("Contact not found.")

    elif action == "delete":
        search = input("Enter the name, you looking for delete: ").lower()
        if search in contacts:
            contacts.pop(search)
            print(f"{search.title()}'s phone is deleted.")
        else:
            print("Contact not found.")

    elif action == "show all":
        if contacts:
            for name, phone in contacts.items():
                print(f"Name: {name.title()}, Phone: {phone}")
        else:
            print("Contact is empty.")
        
    elif action == "exit":
        print("You leave the app.")
        break
    else:
        print("Invalid input, try again.")