from hangman_arts import title, stages
from hangman_words import word_list
import random

def get_guess_remainder(secret_word, guessed_letters):
    guessed_set = set(guessed_letters)
    return ''.join(
        letter if letter in guessed_set else '_' for letter in secret_word
    )

def is_guess_correct(secret_word, guessed_letter):
    return guessed_letter in secret_word

MAX_CHANCE = 6

if __name__ == "__main__":
    chances = 0
    guessed_letters = []
    secret_word = random.choice(word_list)
    print(title)
    print(stages[chances])

    while chances < MAX_CHANCE:
        print(f"Word to guess: {get_guess_remainder(secret_word, guessed_letters)}")
        guessed_letter = input("Guess a letter: ").lower()
        guessed_letters.append(guessed_letter)
        if is_guess_correct(secret_word, guessed_letter):
            remaining_guess = get_guess_remainder(secret_word, guessed_letters)
            print(remaining_guess)
            if '_' not in remaining_guess:
                break
        else:
            print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
            print(f"{MAX_CHANCE-(chances+1)}/{MAX_CHANCE} lives left")
            chances += 1
        print(stages[chances])

    if chances == MAX_CHANCE:
        print("You're dead. Try again next time.")
    else:
        print("You've won the game, you've won the life.")
