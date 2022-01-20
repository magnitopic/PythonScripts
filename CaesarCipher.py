from operator import le


leters = list("abcdefghijklmnopkrstuvwxyz")


def encript(text):
    text = list(text)
    for i in range(len(text)):
        for j in range(len(leters)):
            if text[i] == leters[j]:
                text[i] = leters[j-23]
                break
    return ''.join(text)


def decript(text):
    text = list(text)
    for i in range(len(text)):
        for j in range(len(leters)):
            if text[i] == leters[j]:
                text[i] = leters[j-3]
                break
    return ''.join(text)


if __name__ == "__main__":
    option = input("Do you want to encript or decript?: ").lower()
    if option == "encript":
        text = input("What text do you want to encript?: ").lower()
        print(encript(text))
    elif option == "decript":
        text = input("What text do you want to decript?: ").lower()
        print(decript(text))
