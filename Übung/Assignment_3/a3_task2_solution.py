"""
task4_solution.py
Word count
L.L.
"""

# text = "I study at THI and I have fun. I am in third semester. My Name is Max"
text = "I study at THI and I have fun"

words = text.split(sep=" ")
print(words)

for w in words: 
    count = words.count(w)
    print(f"Frequency of word '{w}': {count}")
