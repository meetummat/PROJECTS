import random

# 1 = Snake
# -1 = Water
# 0 = Gun

computer = random.choice([-1,0,1])
youstr = input("Enter your choice : ")
youDict = {"snake": 1, "water": -1, "gun": 0}

if youstr not in youDict:
    print('Please enter between "snake", "water" and "gun".')
    exit()
you = youDict[youstr]

reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
print(f"You chose : {reverseDict[you]}\nComputer chose : {reverseDict[computer]}")


if computer == you:
    print("it's a draw")
else:
    if computer == 1 and you == -1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == 0 and you == 1:
        print("You lose!")
    elif computer == 0 and you == -1:
        print("You win!")
    else:
        print("Something went wrong!")
