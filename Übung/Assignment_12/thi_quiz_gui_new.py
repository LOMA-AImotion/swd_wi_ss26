# -*- coding: utf-8 -*-

import tkinter as tk
# Sometimes the explicit import is necessary
from tkinter import messagebox
from tkinter import filedialog
#from tkinter import ttk
from PIL import Image, ImageTk 
from functools import partial
from thi_quiz_interfaces import AbstractQuizCore


class QuizGUI:
    def __init__(self, core: AbstractQuizCore, path_to_image="quiz_logo.png", options="ABCD"):
        """
        Args:
            core: Core module (AbstractQuizCore). Must provide get_next_question, reset and check answer
            path_to_image: Path to quiz logo image
            options: String containing the names of the four answer option, e.g. "1234" 
        """
        # This is a type hint, it tells you which datatype this object should have
        self.core: AbstractQuizCore = core

        self.path_to_image = path_to_image

        self.options = options

        self.main_window:tk.Tk = tk.Tk()
    
        self.main_window.title(self.core.name)

        canvas = tk.Canvas(self.main_window, width=600, height = 300)
        canvas.grid(columnspan=2, rowspan=4)

        logo = Image.open(path_to_image)
        # Remove the "self." to see garbage collection in action
        self.logo_tk = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(self.main_window, image=self.logo_tk)
        logo_label.image = logo
        logo_label.grid(row = 0, column = 0, columnspan = 2)

        # question label 
        self.quest_var = tk.StringVar()
        self.quest_var.set("Hi there")

        quest_label = tk.Label(self.main_window, textvariable=self.quest_var, font = ("Arial 18 bold"))

        quest_label.grid(row = 1, column = 0, columnspan = 2)

        self.answer_vars = [tk.StringVar(self.main_window, f"Answer {i}") for i in range(0, 4)]

        for i in range(0, 2):
            for j in range(0, 2):
                answer_button = tk.Button(self.main_window, 
                                        textvariable = self.answer_vars[i * 2 + j], 
                                        font = ("Arial 14"),
                                        # Allows the answered function to be called with the correct index.
                                        # Another solution would involve hardcoding answered functions for
                                        # all 4 buttons with
                                        command = partial(self.answered, i*2 + j)
                                        )
                
                answer_button.grid(row = 2+i, column = j)

    def draw_gui(self):
        """
        Retrieves the next question and updates the texts in the GUI.    
        """

        question = self.core.get_next_question()

        if question is None:
            # No questions left, quiz is finished
            self.exit()

        question_text = question.question # String
        answers = question.answers # list of answers
                
        self.quest_var.set(question_text)
        for k, val in enumerate(answers): 
            self.answer_vars[k].set(self.options[k] + ") " +val.text)

    def answered(self, i):
        """
        Compares the given answer with the solution. 

        Args:
            i: integer, the index (starting at 0) of the given answer.
        """

        print(f"I got the answer {i}")

        # core module is completely responsible for the logic, the GUI module only shows the results!
        if self.core.check_answer(i):
            tk.messagebox.showinfo("Well done", "That is indeed correct, congrats.")   
            self.draw_gui()         
        else:
            tk.messagebox.showerror("Try again", "That was not correct, try again.")

    def run(self):
        self.draw_gui()
        self.main_window.mainloop()

    def exit(self):
        self.main_window.destroy()
        quit()  # quits the whole python program
