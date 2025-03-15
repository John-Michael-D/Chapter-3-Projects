#This is just a simple calculator created with the purpose of allowing the user to perform simple arithmetic.

username = input("Welcome to this simple calculator. I will do my best to assist you with basic arithmetic. Before we begin, what is your name?")

print(f"""\nVery well, {username}.

Here are several options: 

Option 1: Addition (+).
Option 2: Subtraction (-).
Option 3: Multiplication (*).
Option 4: Division (/).

Note that this script will always return a decimal number for all operations.
If you would like to exit the program, you may do so at any time by pressing Ctrl+C.
""")

while True:

    try:
        userchoice = input(f"Now, {username}, select an option (1/2/3/4): ")
        if userchoice not in ["1", "2", "3", "4"]:
            print("Invalid entry! Please enter 1, 2, 3, or 4.")
            continue

        while True:
            try:
                if userchoice == "1":
                    num_1 = float(input(f"{username}, what's the first number you would like to add?"))
                    num_2 = float(input(f"{username}, what's the second number you would like to add?"))
                    result = num_1 + num_2
                    print(f"\n{username}, {num_1} plus {num_2} equals {result}.")
                elif userchoice == "2":
                    num_1 = float(input(f"{username}, what's the first number you would like to subtract?"))
                    num_2 = float(input(f"{username}, what's the second number you would like to subtract?"))
                    result = num_1 - num_2
                    print(f"\n{username}, {num_1} minus {num_2} equals {result}.")
                elif userchoice == "3":
                    num_1 = float(input(f"{username}, what's the first number you would like to multiply?"))
                    num_2 = float(input(f"{username}, what's the second number you would like to multiply?"))
                    result = num_1 * num_2
                    print(f"\n{username}, {num_1} times {num_2} equals {result}.")
                elif userchoice == "4":
                    num_1 = float(input(f"{username}, what's the first number you would like to divide?"))
                    num_2 = float(input(f"{username}, what's the second number you would like to divide?"))
                    if num_2 == 0:
                        print("Error! Division by 0 is not allowed!")
                    else:
                        result = num_1 / num_2
                        print(f"\n{username}, {num_1} divided by {num_2} equals {result}.")
            except ValueError:
                print("Invalid entry! Please enter a valid integer or decimal number.")
                continue
            break

    except KeyboardInterrupt:
        print(f"\nExiting calculator. Goodbye, {username}!")
        break

    restart = input(f"\n{username}, would you like to perform another calculation? (yes/no)").strip().lower()
    if restart not in ["yes", "no"]:
        print("Invalid entry! Enter yes or no.")
    elif restart != "yes":
        print(f"Thank you for using the calculator! Have a good one, {username}.")
        break