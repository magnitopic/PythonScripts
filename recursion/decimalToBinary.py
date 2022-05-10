

def test(num):
    if num == 0:
        return ""
    return test(num//2) + str(num % 2)


if __name__ == "__main__":
    try:
        num = int(input("Enter a whole number: "))
    except:
        print("Invalid value")
    else:
        print(test(num))
