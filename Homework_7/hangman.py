from random import choice


def hangman(word):
    letters = list(word)
    mistakes = 5
    gu = ['_ '] * len(letters)
    while mistakes != 0:
        print('Guess the word. {} mistakes left.'.format(mistakes))
        print(*gu)
        letter = input('Guess a letter: ').lower()
        for i in range(len(letters)):
            if letters[i] == letter:
                gu[i] = letter.upper() + ' '
        if letter not in letters:
            mistakes -= 1
        if '_ ' not in gu:
            print(*gu)
            return print('You won the game.')
    if mistakes == 0:
        return print('You lost the game.')


with open('fruits.txt') as f:
    fruit = f.readlines()
example = choice(fruit).strip()
hangman(example)
