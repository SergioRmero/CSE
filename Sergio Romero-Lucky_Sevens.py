import random
money = 15
level = 0
# level = round
while money > 0:
    print("Lets play Lucky Sevens!")
    print("Bet one dollar to get started!")
    print("Hint: type 1")
    input(">_")
    money -= 1
    level = level + 1
    D1 = random.randint(1, 6)
    D2 = random.randint(1, 6)
    if (D1 + D2) == 7:
        money += 5
        print("You won $5")
    elif (D1 + D2) != 7:
        print("You lost $1")
    print("Money =", money)
    print("Round =", level)
    print("Roll =", D1 + D2)
if money == 0:
    print("Better luck next time!")
