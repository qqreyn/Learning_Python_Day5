import random
print("Guess number from 1 to 10!")
rng = random.randrange(1, 11)

num = int(input("Guess a number: "))

while (num != rng):
    if (num > 10 or num < 1):
        print("Invalid number")
        exit()

    print("Incorrect number, try again!")
    num = int(input("Guess a number: "))
else:
    print("Correct number!")
