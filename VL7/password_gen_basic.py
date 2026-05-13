import random
import tkinter as tk
from string import punctuation


adjectives_path = "adjektive.txt"
nouns_path = "substantive.txt"


def read_file(file):
    with open(file) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def generate_password():
    adjectives = read_file(adjectives_path)
    nouns = read_file(nouns_path)

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(0, 100)
    sc = random.choice(punctuation)

    password = adjective + noun + str(number) + sc
    password_label.config(text=f"Generated Password: {password}")

# Create Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Create and place the Generate Password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

# Create a label to display the generated password
password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()

# Start the Tkinter main loop
root.mainloop()
