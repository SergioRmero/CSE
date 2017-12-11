import random
# Generate a number
# ask the user for an input(number)
# does the guess match the number?
# add "higher" and "lower"
# add 5 guesses
number = random.randint(0,50)

guessesTaken = 0

print("Type a number between 0 and 50")

while guessesTaken < 6:
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Try Again, Guess Higher")

    if guess > number:
        print("Try Again, Guess Lower")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good Job!")

if guess != number:
    number = str(number)
    print("Sorry, the number that I was think of was" + number)