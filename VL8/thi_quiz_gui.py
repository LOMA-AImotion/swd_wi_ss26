import tkinter as tk
from tkinter import messagebox
import random
from functools import partial

all_quiz_questions = None
correct_answer_index = None

def draw_gui():
    current_question = random.choice(all_quiz_questions)
    question_text, answers, correct_index = current_question
    label.config(text=question_text)

    global correct_answer_index
    correct_answer_index = correct_index

    for b, a in zip(answer_buttons, answers):
        b.config(text=a)

def answered(button_index):
    if button_index == correct_answer_index: 
        messagebox.showinfo("Well done!!", "That is correct, congrats!")
        draw_gui()
    else: 
        messagebox.showerror("WRONG", "Sorry, that was not correct :(")

main_window = tk.Tk()
main_window.title("THI Quiz")
main_window.geometry("800x600")
canvas = tk.Canvas(main_window, width=800, height=600)
canvas.grid(row=0, column=0, rowspan=4, columnspan=2)
testfrage = "Wie heißt die Hauptstadt von Bayern?"
label = tk.Label(main_window, text=testfrage, font=("Arial", 14))
label.grid(row=1, column=0, columnspan=2)
testantworten = ["München", "Nürnberg", "Augsburg", "Ingolstadt"]

answer_buttons = []
for i, antwort in enumerate(testantworten):
    button = tk.Button(main_window, text=antwort, command=partial(answered, i))
    answer_buttons.append(button)
    button.grid(row=i // 2 + 2, column=i % 2)
