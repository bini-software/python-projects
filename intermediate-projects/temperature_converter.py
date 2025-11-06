def convert_temprature():

    while True:
        print("\n1. Convert to Celsius")
        print("2. Convert to Fahrenheit")
        print("3. Convert to Kelvin")
        print("4. Exit")

        choice = input("\nChoose an option(1-4) or type by word: ").lower()
        if choice == "4" or choice == "exit":
            print("Exiting... Goodbye!")
            break
        
        user_temp = input("What is your curremt unit?\nType (1. Celsius, 2. Fahrenheit, 3. Kelvin): ").lower()
        temp = float(input("Enter your temprature value: "))

        if choice == "1" or choice == "convert to celsius":
            if user_temp == "fahrenheit" or user_temp == "2":
                result = 5/9 * (temp - 32)
            elif user_temp == "kelvin" or user_temp == "3":
                result = temp - 273.15
            elif user_temp == "celsius" or user_temp == "1":
                result = temp
            else:
                print("Error. Invalid unit")
                continue
            print(f"Result: {result:.2f} °C")

        elif choice == "2" or choice == "convert to fahrenheit":
            if user_temp == "celsius" or user_temp == "1":
                result = 9/5 * temp + 32
            elif user_temp == "kelvin" or user_temp == "3":
                result = 9/5 * (temp - 273.15) + 32
            elif user_temp == "fahrenheit" or user_temp == "2":
                result = temp
            else:
                print("Error. Invalid unit")
                continue
            print(f"Result: {result:.2f} °F")
        
        elif choice == "3" or choice == "convert to kelvin":
            if user_temp == "celsius" or user_temp == "1":
                result = temp + 273.15
            elif user_temp == "fahrenheit" or user_temp == "2":
                result = 5/9 * (temp - 32) + 273.15
            elif user_temp == "kelvin" or user_temp == "3":
                result = temp
            else:
                print("Error. Invalid unit")
                continue
            print(f"Result: {result:.2f} K")
        else:
            print("Invalid choice. Try again")

convert_temprature()