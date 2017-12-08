import random
# Generate a number
# ask the user for an input(number)
# does the guess match the number?
# add "higher" and "lower"
# add 5 guesses
number = random.randint(0,50)

guesses_used = 0

if guesses_used != 5:
    print("Type in a number between 0 and 50")
while True:
    guess = int(input("Guess: "))
    if guess > number:
        print("Try Again, Guess Lower!")
    elif guess < number:
        print("Try Again, Guess Higher!")
    elif guess == number:
        break


print("Good Job!")
