#Jeffery Morning Star
#CIS256 Fall 2026
#Programming Assignment 4

import random

#List of words
word_list = ["random", "bridge", "maelstrom", "imposter", "overalls"]

def select_word():
    return random.choice(word_list)

def check_guess(guess, secret_word):
    if guess in secret_word:
        return True
    else:
        return False

#select a random word
secret_word = random.choice(word_list)

#variables
guessed_letters = []
attempts = 6
words_guessed = False

print("This is the word guessing game!")
print("Guess the word one letter at a time.")
print("You have ", attempts ," guesses available.")

while attempts > 0 and not words_guessed:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_"

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", attempts)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("The letter ", guess, " is in the word!")
    else:
        print("The letter ", guess, " is not in this word.")
        attempts -= 1

    words_guessed = all(letter in guessed_letters for letter in secret_word)

if words_guessed:
    print("Congratulations! You guessed the word: ", secret_word)
else:
    print("Game over. You have run out of attempts.")
    print("The correct word was: ", secret_word)
