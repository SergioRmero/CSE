word_bank = ['name', 'science', 'election', 'overeat', 'dramatic', 'revoke', 'positive', 'tide', 'knuckles', 'victory']
shown_word = ['_'] * len(word_bank)
Input = ">_"
lives = 10
letter_number = 0
correct_guesses = 0

while lives != 0:
    print("The word is:" + str(shown_word))
    print("You have " + str(lives) + " lives left")
    Input = raw_input("Enter guess: ")

    while letter_number < len(word_bank):
        if word_bank[letter_number] == Input:
            shown_word[letter_number] = Input
            correct_guesses += 1
        letter_number += 1

    lives -= 1

    if correct_guesses == len(word_bank):
        print("You won!")
        break

    if lives == 0:
        print("You lost")
        print()
