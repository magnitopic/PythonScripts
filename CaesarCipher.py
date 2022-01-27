from itertools import cycle


leters = list("abcdefghijklmnñopkrstuvwxyz")


def encript(text, rotations):
    text = list(text)
    for i in range(len(text)):
        for j in range(len(leters)):
            if text[i] == leters[j]:
                text[i] = leters[j-len(leters)+rotations]
                break
    return ''.join(text)


def decript(text, rotations):
    text = list(text)
    for i in range(len(text)):
        for j in range(len(leters)):
            if text[i] == leters[j]:
                text[i] = leters[j-rotations]
                break
    return ''.join(text)


if __name__ == "__main__":
    option = input("Do you want to encript or decript?: ").lower()
    rotations = int(input("How may rotations?: "))
    if option == "encript":
        text = input("What text do you want to encript?: ").lower()
        print(encript(text, rotations))
    elif option == "decript":
        text = input("What text do you want to decript?: ").lower()
        print(decript(text, rotations))
