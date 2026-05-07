"""
Implements a function that checks whether a given string is a palindrome or not.
"""

def is_palindrome(text):
    text = text.lower() # converts the text to lowercase
    print("lower", text)

    cleaned_text = ""
    for character in text:
        if character.isalpha(): # checks if the character is alphabetic
            cleaned_text = cleaned_text + character
            
    print(cleaned_text)
    cleaned_text_reversed = cleaned_text[::-1]
    print(f"Cleaned reversed: {cleaned_text_reversed}")
    return cleaned_text == cleaned_text_reversed

examples = ["anna", "Anna", "Step on no pets", "Mr. Owl ate my metal worm.", "Test! if? it works"]

for e in examples:
    print(f"Is '{e}' a palindrome? {is_palindrome(e)}")
