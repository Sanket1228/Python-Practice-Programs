n = 25
number_of_guess = 1
while number_of_guess <= 9:
    number = int(input("Enter your number : "))
    if number < n:
        print(f"Your guessed number is less than actual number\nYou have {9-number_of_guess} chances left")
    elif number > n:
        print(f"Your guessed number is greater than actual number\nYou have {9-number_of_guess} chances left")
    else:
        print(f"You guessed the number right\nYou found it in {number_of_guess} chance")
        break
    number_of_guess = number_of_guess + 1

if number_of_guess>9:
    print("GAME OVER...")    

