import tkinter
from tkinter import simpledialog, messagebox
import random

def setup():
    global remaining_guesses
    remaining_guesses = num_guesses
    global solution_word
    solution_word = random.choice(wordlist)
    global guessed_characters
    guessed_characters = set()
    label_word.set(hangman_string_function(solution_word, guessed_characters))
    label_remaining_guesses.set(str(remaining_guesses))


def create_hangman_string(solution, guesses):
    result = ""
    
    for character in solution:
        if character in guesses:
            result += character + " " # whitespace only for cosmetic reasons
        else:
            result += '_ ' 
            
    return result


def clean_string_from_whitespaces(string):
    return string.replace(" ", "")


def guess_and_update_text():
    guess = tkinter.simpledialog.askstring("Guess", "Enter guess", parent=main_win)
    print(guess)
    
    # Lazy evaluation!
    while guess is None or len(guess) != 1 or not guess.isalpha(): 
        guess = tkinter.simpledialog.askstring("Guess", "Your guess must be a single character!", parent=main_win)

    guessed_characters.add(guess.upper())

    current_hangman_string = hangman_string_function(solution_word, guessed_characters)
    label_word.set(current_hangman_string)
    
    # I added whitspaces to the hangman string for better looks,
    # thats why we have to clean it from whitespaces
    if solution_word == clean_string_from_whitespaces(current_hangman_string):
        tkinter.messagebox.showinfo("Congratulations!",  "You won the game!")
        setup_function()
        return

    if guess.upper() not in solution_word.upper():
        global remaining_guesses
        remaining_guesses -= 1
        label_remaining_guesses.set(str(remaining_guesses))

    if remaining_guesses == 0:
        tkinter.messagebox.showinfo("Sorry!", "You lost!")
        setup_function()
        return


######## config ###########
wordlist = ["HELLO", "THI", "SOFTWARE", "DEVELOPMENT", "TEST", "HANGMAN"]
num_guesses = 11
remaining_guesses = None
solution_word = None
guessed_characters = None

# Callback to the function, makes it easier to change later 
hangman_string_function = create_hangman_string
setup_function = setup
##########################


main_win = tkinter.Tk()
main_win.title("SWD Hangman")

# label.config(text=...) would work as well
label_word=tkinter.StringVar()
tkinter.Label(main_win, textvariable=label_word, font=("Consolas 24 bold")).grid(row=0, column=1, columnspan=2, padx=10)
tkinter.Label(main_win, text="Remaining\nguesses", font=("Consolas 16 bold")).grid(row=0, column=0)

label_remaining_guesses = tkinter.StringVar()
tkinter.Label(main_win, textvariable=label_remaining_guesses, font=("Consolas 16 bold")).grid(row=1, column=0)

tkinter.Button(main_win, text="Enter Guess", command=guess_and_update_text).grid(row=1, column=1)
tkinter.Button(main_win, text="New Game", command=setup_function).grid(row=1, column=2)

setup_function()
main_win.mainloop()