""" 
Working with palindromes using recusrion
"""

def reverseString(text):
    if text == "":return ""
    return reverseString(text[1:len(text)]) + text[0]


def checkIfPalindrome(text):
    return text == reverseString(text)


if __name__ == "__main__":
    text = input("Please enter a word: ").strip().lower() or "tacocat"
    if checkIfPalindrome(text):
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")
