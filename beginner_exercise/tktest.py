import tkinter as tk
import random

number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts

    try:
        guess = int(entry.get())
    except ValueError:
        result.config(text="Please enter a valid number.")
        return

    attempts += 1

    if guess < number:
        result.config(text="Try Greater")
    elif guess > number:
        result.config(text="Try Smaller")
    else:
        result.config(
            text=f"🎉 Correct! You guessed it in {attempts} attempts."
        )
        button.config(state="disabled")

    entry.delete(0, tk.END)

# Create window
root = tk.Tk()
root.title("Guess the Number")
root.geometry("350x200")

# Widgets
title = tk.Label(root, text="Guess a number between 1 and 100")
title.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Guess", command=check_guess)
button.pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()