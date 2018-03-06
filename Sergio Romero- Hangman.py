import random

# This is a guide how to make hangman
# 1. Make word bank - 10 items
# 2. Select a random item to guess
# 3. Take in a letter and add it to a list of letters_guessed, hide it and reveal letters
# 4. Reveal letters based on input
# 5. Create win and lose conditions


word_bank = ['name', 'science', 'election', 'overeat', 'dramatic', 'revoke', 'positive', 'tide', 'knuckles', 'victory']
chosen = random.choice(word_bank)
shown_word = ['*'] * len(chosen)
Input = ">_"
lives = 10
letter_number = 0
correct_guesses = 0



while lives != 0:
    print("The word is:" + str(shown_word))
    print("You have " + str(lives) + " lives left")
    Input = input("Enter guess: ")

    while letter_number < len(chosen):
        if chosen[letter_number] == Input:
            shown_word[letter_number] = Input
            correct_guesses += 1
        letter_number += 1

    lives -= 1

    if correct_guesses == len(chosen):
        print("You won!")
        break

    if lives == 0:
        print("You lost")
        print("The word was " + chosen)
