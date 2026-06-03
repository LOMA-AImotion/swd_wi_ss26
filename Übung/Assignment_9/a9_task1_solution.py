# -*- coding: utf-8 -*-
"""
a9_task1_solution.py

Implements a core functionality for the hangman game.
"""

def create_hangman_string(solution, guesses):
    result = ""
    
    for character in solution:
        if character in guesses:
            result += character
        else:
            result += '_'
            
    return result

solution = "Hello"
guesses = ["H", "o"]

print(create_hangman_string(solution, guesses))