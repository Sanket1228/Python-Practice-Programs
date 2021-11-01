import random
lst = ['s','w','g']

chances = 0
comp_point = 0
user_point = 0

while chances < 10:
    user_ch = input("Enter Your Choice ('s' for Snake, 'w' for Water, 'g' for Gun) : ")
    comp_ch = random.choice(lst)

    if comp_ch == user_ch:
        print("0 point for computer and human")
    elif comp_ch == "s" and user_ch == "w":
        print("Computer is winner")
        print(f"Because Computer's choice is {comp_ch} and Human Choice is {user_ch}")
        comp_point += 1
    elif comp_ch == "w" and user_ch == "g":
        print("Computer is winner")
        print(f"Because Computer's choice is {comp_ch} and Human Choice is {user_ch}")
        comp_point += 1
    elif comp_ch == "g" and user_ch == "s":
        print("Computer is winner")
        print(f"Because Computer's choice is {comp_ch} and Human Choice is {user_ch}")
        comp_point += 1
    elif user_ch == "s"and comp_ch == "w":
        print("Human is winner")
        print(f"Because Computer's choice is {comp_ch} and Human Choice is {user_ch}")
        user_point += 1
    elif user_ch == "w"and comp_ch == "g":
        print("Human is winner")
        print(f"Because Computer's choice is {comp_ch} and Human Choice is {user_ch}")
        user_point += 1
    elif user_ch == "g"and comp_ch == "s":
        print("Human is winner")
        print(f"Because Computer's choice is {comp_ch} and Human Choice is {user_ch}")
        user_point += 1
    chances += 1

if comp_point == user_point:
    print("Competition is tie")
    print(f"Both players are having {comp_point} points")
elif comp_point > user_point:
    print("Computer won the competition")
    print(f"Because computer's points are {comp_point} and Human's points are {user_point}")
elif comp_point < user_point:
    print("Human won the competition")
    print(f"Because computer's points are {comp_point} and Human's points are {user_point}")

print("Hope you enjoyed the game !!!!!!")

