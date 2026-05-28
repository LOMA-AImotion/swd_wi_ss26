# -*- coding: utf-8 -*-
"""
thi_quiz_data.py

Created on Tue Nov 23 22:27:53 2021

@author: 
"""

def load_questions_from_file(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    file.close()

    # with open(file_path, "r") as file:
    #     lines = file.readlines()

    num_questions = int(lines[0])
    all_questions = []

    for i in range(1, num_questions*5, 5):
        question_text = lines[i]
        answers = [lines[i+j] for j in range(1, 5)]
        answers = [a.replace("\n", "") for a in answers]

        correct_index = None

        for index, answer in enumerate(answers):
            if answer.startswith("CORRECT"):
                correct_index = index
                cleaned_answer = answer.replace("CORRECT:", "")
                answers[index] = cleaned_answer

        question = (question_text, answers, correct_index)
        all_questions.append(question)

    return all_questions

if __name__ == "__main__":
    print(load_questions_from_file("quiz_functions.txt"))