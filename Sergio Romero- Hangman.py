import random

# This is a guide how to make hangman
# 1. Make word bank - 10 items
# 2. Select a random item to guess
# 3. Take in a letter and add it to a list of letters_guessed, hide it and reveal letters
# 4. Reveal letters based on input
# 5. Create win and lose conditions


word = ['name', 'science', 'election', 'overeat', 'dramatic', 'revoke', 'positive', 'tide', 'knuckles', 'victory']
lives = 10
one_st = []  # the list where the characters of your word goes
u_ls = []  # the list where the players guesses go

chosen = random.choice(word)  # chooses a random word from your list


print(one_st)
while True:
    shrug = input("Guess a letter :")  # the users input
    for letter in chosen:
        one_st.append(letter)  # adds the letter to the list
        u_ls.append('*')  # adds a * for every letter in your word
