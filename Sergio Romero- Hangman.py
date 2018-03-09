import random

word_bank = ['name', 'science', 'election', 'overeat', 'dramatic', 'revoke', 'positive', 'tide', 'knuckles', 'victory']
chosen = random.choice(word_bank)
shown_word = '*' * len(chosen)
Input = ">_"
lives = 10
letter_number = 0
correct_guesses = 0

while lives != 0:
    print("The word is:" + str(shown_word))
    print("You have " + str(lives) + " lives left")
    Input = raw_input("Enter guess: ")

    while letter_number < len(chosen):
        if chosen[letter_number] == chosen:
            list(shown_word)[letter_number] = chosen
            correct_guesses += 1
        letter_number += 1

    lives -= 1

    if correct_guesses == len(chosen):
        print("You won!")
        break

    if lives == 0:
        print("You lost")
        print("The word was " + chosen)
