import thi_quiz_data 
import thi_quiz_gui

if __name__ == "__main__":
    print("Starting the quiz application ...")
    quiz_questions = thi_quiz_data.load_questions_from_file("quiz_functions.txt")
    thi_quiz_gui.all_quiz_questions = quiz_questions
    thi_quiz_gui.draw_gui()
    thi_quiz_gui.main_window.mainloop()