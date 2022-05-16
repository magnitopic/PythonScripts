""" This program writes a book with random words that have the same
	length as the digit of Pi(π) that's in that position. Example:
	First word would have 3 letters, second 1, third 4... and so on.
"""
import requests, random
from mpmath import mp


def newPiBook(nWords=100):
    book = ""
    # Source for all words in the English laguage:
    # https://github.com/dwyl/english-words
    request = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
    # parse data to make a list of words
    words = str(request.text).strip().split("\n")

    # pi characters we need
    mp.dps = nWords
    # list of pi numbers
    piNum = list(str(mp.pi).replace(".", ""))

    for i in piNum:
        # Get all words that have the correct length
        wordList = ["."]
        for word in words:
            if len(word) == int(i):
                wordList.append(word.lower())
        # Pic a random word from the list
        if (choice := random.choice(wordList)) == ".":
            book += choice
        else:
            book += " "+choice
    return book.strip().capitalize()


if __name__ == "__main__":
    print(newPiBook())
