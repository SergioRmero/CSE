import random
money = 15
round = 0
print("Lets play Lucky Sevens!")
print("Bet one dollar to get started!")
print("Hint: type 1")
one_dollar = input(">_")
money -= 1

while money != 0:
    D1 = random.randint(1, 6)
    D2 = random.randint(1, 6)
    print("You won your bet back plus $4!")
    if D1 + D2 == 7:
        money += 5
    elif D1 + D2 != 7:
        print("You lost $1")
    round += 1
    break
print("Roll", )
print("Money Left", money)
