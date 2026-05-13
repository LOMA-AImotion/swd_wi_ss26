from thi_util import generate_password
import tkinter as tk

adjectives_path = "adjektive.txt"
nouns_path = "substantive.txt"

def trigger_pw_gen():
    pw = generate_password(adjectives_path, nouns_path)
    password_label.config(text=f"Generated Password: {pw}" )

# Create Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Create and place the Generate Password button
generate_button = tk.Button(root, text="Generate Password", command=trigger_pw_gen)
generate_button.pack(pady=20)

# Create a label to display the generated password
password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()

# Start the Tkinter main loop
root.mainloop()

