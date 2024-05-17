import random
import tkinter as tk


def start_game():
    menu_frame.pack_forget()
    guess_game.pack()
    new_game()


def new_game():
    global word, allowed_errors, guesses, done
    word = random.choice(words).strip().lower()
    allowed_errors = 7
    guesses = []
    done = False
    update_word_display()
    errors_label.config(text=f"Chances left: {allowed_errors}")
    result_label.config(text="")


def check_guess(event=None):
    global allowed_errors, done
    if done:
        return

    guess = guess_entry.get().strip().lower()
    guess_entry.delete(0, tk.END)

    if not guess.isalpha():
        result_label.config(text="Invalid character!")
        return

    if guess in guesses:
        result_label.config(text="You already guessed that letter!")
        return

    guesses.append(guess)

    if guess not in word:
        allowed_errors -= 1
        errors_label.config(text=f"Chances left: {allowed_errors}")
        if allowed_errors == 0:
            done = True
            result_label.config(text=f"Game over! The word was {word}")
            show_retry_quit_buttons()
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
    word_label.config(text=word_display.strip())
    if not '_' in word_display:
        done = True
        result_label.config(text="You won!")
        show_retry_quit_buttons()


def show_retry_quit_buttons():
    guess_button.pack_forget()
    retry_button.pack(pady=5)
    quit_button.pack(pady=5)


def retry_game():
    new_game()
    retry_button.pack_forget()
    quit_button.pack_forget()
    guess_button.pack(pady=5)


def quit_game():
    root.destroy()


with open('wordlist.txt', 'r') as f:
    words = f.readlines()


root = tk.Tk()
root.title("Guessing Game")


menu_frame = tk.Frame(root)
menu_frame.pack()

description_label = tk.Label(menu_frame, text="Welcome to Guessing Game!\n\n\n\nInstructions:\n\nGuess the word by entering one letter at a time. You are given 7 chances.\n\nOnly use Alphabets. Good Luck!!", font=("Arial", 14))
description_label.pack(padx=10, pady=10)

play_button = tk.Button(menu_frame, text="Play", font=("Arial", 14), command=start_game)
play_button.pack(pady=5)

# Game Frame
guess_game = tk.Frame(root)

# Game variables
allowed_errors = 7
guesses = []
done = False

# Labels
word_label = tk.Label(guess_game, text="", font=("Arial", 18))
word_label.pack(pady=10)

errors_label = tk.Label(guess_game, text=f"Chances left: {allowed_errors}", font=("Arial", 12))
errors_label.pack(pady=5)

result_label = tk.Label(guess_game, text="", font=("Arial", 14))
result_label.pack(pady=10)


guess_entry = tk.Entry(guess_game, font=("Arial", 14))
guess_entry.pack(pady=5)


guess_button = tk.Button(guess_game, text="Guess", font=("Arial", 14), command=check_guess)
guess_button.pack(pady=5)

retry_button = tk.Button(guess_game, text="Retry", font=("Arial", 14), command=retry_game)

quit_button = tk.Button(guess_game, text="Quit", font=("Arial", 14), command=quit_game)

root.bind('<Return>', check_guess)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = screen_width // 2
window_height = screen_height // 2
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

root.mainloop()
