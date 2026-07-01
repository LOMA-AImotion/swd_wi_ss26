# -*- coding: utf-8 -*-

import thi_quiz_data_new as data
import thi_quiz_gui_new as gui
import thi_quiz_core as core

# Here we create actual instances of our objects and put everything together
# The individual components are only connected here

all_questions = data.load_questions_from_file("quiz_functions.txt")
sequence_generator = data.QuestionSequenceGenerator(all_questions)

path_to_img = "quiz_logo.png"

core = core.QuizCore(sequence_generator, name="SWD Quiz")

quiz = gui.QuizGUI(core, path_to_image=path_to_img)
quiz.run()
