"""
a2_task2_solution.py
Demonstrates several list operations
L.L.
"""

num_words = int(input("How many words do you want to input? "))
word_list = []

for i in range(num_words):
    word = input(f"Please input word no. {i+1}: ")
    word_list.append(word)

character_sum = 0

print(word_list)

for word in word_list:
    for char in word:
        print(char)
    character_sum = character_sum + len(word) 
    # This is equivalent:
    # character_sum += len(word)
    
print(f"All words had a total length of {character_sum}.")
# This print statement is equivalent:
print("All words had a total length of", character_sum)
