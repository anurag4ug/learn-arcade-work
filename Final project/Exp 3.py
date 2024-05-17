import random
import tkinter as tk


def start_game():
    # Hide the menu and start the game
    menu_frame.pack_forget()
    hangman_frame.pack()
    new_game()


def new_game():
    global word, allowed_errors, guesses, done
    word = random.choice(words).strip().lower()
    allowed_errors = 7
    guesses = []
    done = False
    update_word_display()
    errors_label.config(text=f"Allowed errors left: {allowed_errors}")


def check_guess(event=None):
    global allowed_errors, done
    if done:
        return

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
        if letter in guesses:
            word_display += letter + " "
        else:
            word_display += "_ "
            if letter not in guesses:
                done = False
    word_label.config(text=word_display)
    if not '_' in word_display:
        done = True
        result_label.config(text="You won!")


# Load word list
with open('wordlist.txt', 'r') as f:
    words = f.readlines()

# Initialize GUI
root = tk.Tk()
root.title("Hangman Game")

# Menu Frame
menu_frame = tk.Frame(root)
menu_frame.pack()

description_label = tk.Label(menu_frame,
                             text="Welcome to Hangman Game!\n\nInstructions:\nGuess the word by entering one letter at a time. You have 7 allowed errors. Good luck!",
                             font=("Arial", 14))
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

# Bind the Enter key to check_guess function
root.bind('<Return>', check_guess)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x_coordinate = (screen_width - root.winfo_reqwidth()) // 2
y_coordinate = (screen_height - root.winfo_reqheight()) // 2

# Set the position of the window
root.geometry("+{}+{}".format(x_coordinate, y_coordinate))

root.mainloop()
