import random

word_bank = ['name', 'science', 'election', 'overeat', 'dramatic', 'revoke', 'positive', 'tide', 'knuckles', 'victory']
chosen = random.choice(word_bank)
lives = 10
word_list = list(chosen)
<<<<<<< HEAD
=======
print(word_list)
>>>>>>> c0da1d7102cc9a195764fc32dc5cdbaf8d941a62
shown_word = []
for letter in chosen:
    shown_word.append("*")
while lives != 0:
    temporary_list = []
    print("The word is: " + ''.join(shown_word))
    print("You have " + str(lives) + " lives left")
    Input = input("Enter guess: ")
    for letter1, letter2 in zip(word_list, shown_word):
        if Input == letter1:
            temporary_list.append(Input)
        elif letter2 != "*":
            temporary_list.append(letter2)
        else:
            temporary_list.append("*")
    shown_word = temporary_list

    if lives == 0:
        print("You lost")
        print("The word was " + chosen)
        break
