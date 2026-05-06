"""
a5_task2.py

Implements an encryption in a self-defined secret language.
"""

alphabet = {"a": "b", "b": "c", "c": "d", "d": "e", "e": "f",
            "f": "g", "g": "h", "h": "i", "i": "j", "j": "k",
            "k": "l", "l": "m", "m": "n", "n": "o", "o": "p",
            "p": "q", "q": "r", "r": "s", "s": "t", "t": "u",
            "u": "v", "v": "w", "w": "x", "x": "y", "y": "z",
            "z": "a", " ": " ", ".": ".", "!": "!", "?": "?"}

def encrypt(word, alphabet):
    encrypted_word = ""

    for l in word:
        # same as encrypted_word = encrypted_word + alphabet[l]
        encrypted_word += alphabet[l]

    return encrypted_word

def decrypt(word, alphabet):
    # decrypt using the encrypt function, inverting the alphabet is done in the function

    inverse_alphabet = {v: k for k, v in alphabet.items()}

    return encrypt(word, inverse_alphabet)

############# alternative #########################

def translate(word, alphabet):
    # one general translate function, the two alphabets are managed outside of the function

    translated_word = ""

    for l in word:
        translated_word += alphabet[l]

    return translated_word
####################################################

user_input = input("Please enter a word for encryption: ")

encrypted_input = encrypt(user_input, alphabet)
print(f"{user_input} looks like this when encrypted: {encrypted_input}.")
decrypted_input = decrypt(encrypted_input, alphabet)
print(f"{encrypted_input} looks like this when decrypted: {decrypted_input}.")
