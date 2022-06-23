import random

print("You are now going to be hacked, do you consent? (Y,N)")
print("HAHAHHAHA, nevermind your consent was never neccessary")
print("Your IP is as follows:")

fakeip = ""
for x in range(4):
    fakeip += str(random.randint(0, 999))+"."

print(fakeip[:-1])
