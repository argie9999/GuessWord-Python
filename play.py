import random

words = ['sheetrock', 'mountain', 'marker', 'dice', 'book', 'table', 'dress', 'banana', 'dog']
all_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
guessed_letters = []

def choose_word():
    low = 0
    high = len(words) - 1
    item = random.randint(low, high)
    return words[item]
#end choose_word

def build_word_puzzle(word):
    list = []
    for letter in word:
        list.append('_')
    return ' '.join(list)
#end build_word_puzzle

def show_puzzle(puzzle_word):
    print(puzzle_word)
#end show_word

def show_available():
    available_letters = find_non_guessed()
    print("")
    print("Available Letters: ")
    print(', '.join(available_letters))
    print("")
#end show_available

def find_non_guessed():
    list = []
    for letter in all_letters:
        if letter not in guessed_letters:
            list.append(letter)
    return list
#end find_non_guessed

def replace_str_index(puzzle_word, index, guess):
    puzzle_word = puzzle_word.replace(" ", "")
    list = []
    for i in range(len(puzzle_word)):
        if puzzle_word[i] == '_':
            if i == index:
                list.append(guess.upper())
            else:
                list.append(puzzle_word[i])
        else:
            list.append(puzzle_word[i])

    return ' '.join(list)
#end replace_str_index

def check_guess(guess, word, puzzle_word):
    guessed_letters.append(guess.upper())

    for index in range(len(word)):
        word_letter = word[index]

        if word_letter.upper() == guess.upper():
            puzzle_word = replace_str_index(puzzle_word, index, guess)

    return puzzle_word
#end check_guess


# 1. Pick a word
word = choose_word()
puzzle_word = build_word_puzzle(word)
won_game = False

for guess_index in range(10):
    # 2. Show the word to the player
    show_puzzle(puzzle_word)
    show_available()

    # 3. Let them guess a letter
    guess = raw_input("Guess a letter: ")

    # 4. Check to see if guess is correct
    puzzle_word = check_guess(guess, word, puzzle_word)

    if '_' not in puzzle_word:
        print('Congratulations! You guessed the word: ' + word.upper())
        won_game = True
        break

if won_game == False:
    print('Sorry, you did not guess the word: ' + word.upper())
