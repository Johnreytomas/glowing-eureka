import tkinter as tk
from tkinter import messagebox
import random

word_to_guess = ['apples', 'ladder', 'banana', 'digits', 'bishop', 'laptop']

hangman_images = [
    """
       +---+
           |
           |
           |
          ===
    """,
    """
       +---+
       O   |
           |
           |
          ===
    """,
    """
       +---+
       O   |
       |   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\\  |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===
    """,
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ===
    """
]

current_word = ''
current_guess = []
incorrect_guesses = 0


def choose_word():
    return random.choice(word_to_guess)


def handle_guess(guess):
    global incorrect_guesses
    global current_guess

    if guess in current_word:
        for i in range(len(current_word)):
            if current_word[i] == guess:
                current_guess[i] = guess
    else:
        incorrect_guesses += 1

    img_label.config(text=hangman_images[incorrect_guesses])

    guess_label.config(text=' '.join(current_guess))

    if ''.join(current_guess) == current_word:
        messagebox.showinfo("Hangman", "Congratulations! You won!")
        reset_game()
    elif incorrect_guesses == len(hangman_images) - 1:
        messagebox.showinfo("Hangman", "Game Over! The word was: " + current_word)
        reset_game()


def reset_game():
    global incorrect_guesses
    global current_word
    global current_guess

    incorrect_guesses = 0
    current_word = choose_word()
    current_guess = ["_"] * len(current_word)

    img_label.config(text=hangman_images[incorrect_guesses])

    guess_label.config(text=' '.join(current_guess))


window = tk.Tk()
window.title("Hangman")

current_word = choose_word()
current_guess = ["_"] * len(current_word)

img_label = tk.Label(window, text=hangman_images[incorrect_guesses])
img_label.pack()

guess_label = tk.Label(window, text=' '.join(current_guess))
guess_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

guess_button = tk.Button(window, text="Guess", command=lambda: handle_guess(guess_entry.get()))
guess_button.pack()

reset_button = tk.Button(window, text="Reset", command=reset_game)
reset_button.pack()

window.mainloop()
