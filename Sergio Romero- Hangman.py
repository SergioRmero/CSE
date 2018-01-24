import random

# This is a guide how to make hangman
# 1. Make word bank - 10 items
# 2. Select a random item to guess
# 3. Take in a letter and add it to a list of letters_guessed, hide it and reveal letters
# 4. Reveal letters based on input
# 5. Create win and lose conditions


word = "name", "science", "election", "over eat", "dramatic", "revoke", "positive", "tide", "knuckles", "victory"
guesses = 10

letters_guessed = 0
lol = random.choice(word)
strOne = lol
listOne = list(strOne)
print(listOne)

while guesses != 0:
    input("Guess a letter >")