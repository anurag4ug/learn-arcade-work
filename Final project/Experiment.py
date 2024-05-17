import random
import tkinter as tk

def start_game():
    # Hide the menu and start the game
    menu_frame.pack_forget()
    hangman_frame.pack()

def check_guess():
    global allowed_errors, done
    guess = guess_entry.get().strip().lower()
    guess_entry.delete(0, tk.END)
    guesses.append(guess)

    if guess not in word:
        allowed_errors -= 1
        errors_label.config(text=f"Allowed errors left: {allowed_errors}")
        if allowed_errors == 0:
            done = True
            result_label.config(text=f"Game over! The word was {word}")
    else:
        update_word_display()

def update_word_display():
    global done
    word_display = ""
    for letter in word:
        if letter.lower() in guesses:
            word_display += letter + " "
        else:
            word_display += "_ "
            if letter.lower() not in guesses:
                done = False
    word_label.config(text=word_display)
    if done:
        result_label.config(text=f"You found the word! It was {word}")

# Load word list
with open('wordlist.txt', 'r') as f:
    words = f.readlines()
word = random.choice(words).strip()

# Initialize GUI
root = tk.Tk()
root.title("Hangman Game")

# Menu Frame
menu_frame = tk.Frame(root, width=400, height=800)  # Adjust width and height as needed
menu_frame.pack(pady=200)

description_label = tk.Label(menu_frame, text="Welcome to Hangman Game!\n\nInstructions:\nGuess the word by entering one letter at a time. You have 7 allowed errors. Good luck!", font=("Arial", 14))
description_label.pack(padx=10, pady=10)

play_button = tk.Button(menu_frame, text="Play", font=("Arial", 14), command=start_game)
play_button.pack(pady=5)

# Game Frame
hangman_frame = tk.Frame(root)

# Game variables
allowed_errors = 7
guesses = []
done = False

# Labels
word_label = tk.Label(hangman_frame, text="", font=("Arial", 18))
word_label.pack(pady=10)

errors_label = tk.Label(hangman_frame, text=f"Allowed errors left: {allowed_errors}", font=("Arial", 12))
errors_label.pack(pady=5)

result_label = tk.Label(hangman_frame, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Entry field for guesses
guess_entry = tk.Entry(hangman_frame, font=("Arial", 14))
guess_entry.pack(pady=5)

# Button to submit guesses
guess_button = tk.Button(hangman_frame, text="Guess", font=("Arial", 14), command=check_guess)
guess_button.pack(pady=5)

root.mainloop()
