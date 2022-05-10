from recursion.palindorme import checkIfPalindrome

f = open("quijote.txt")
book = f.read().strip('!"(),-.:;?¡¿').split()
text = []
for letra in book:
    if checkIfPalindrome(letra) and len(letra) > 1:
        print(letra)
f.close()
