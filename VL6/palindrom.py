def is_palindrome(text: str) -> bool: 
    for i in range(0, len(text) // 2): 
        if text[i] != text[len(text) - 1 - i]:
            return False
        
    return True

def is_palindrome2(text: str) -> bool:
    return text == text[::-1]

print("Ist Palindrom anna?", is_palindrome("anna"))
print("Ist Palindrom Anna?", is_palindrome("Anna"))
print("Ist Palindrom gnubelebung?", is_palindrome("gnubelebung"))

print("Ist Palindrom anna?", is_palindrome2("anna"))
print("Ist Palindrom Anna?", is_palindrome2("Anna"))
print("Ist Palindrom gnubelebung?", is_palindrome2("gnubelebung"))