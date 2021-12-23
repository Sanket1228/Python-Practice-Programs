user_input = int(input("Enter you age or birth year : "))

if len(str(user_input)) == 2:
    print(f"You will be 100 years old after {100-user_input} years.")  
elif len(str(user_input)) == 4:
    if user_input > 2021:
        print("You are not born yet....")
        