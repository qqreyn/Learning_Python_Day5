import random
print("Guess the number from 1 to 20, only 5 attempts with hints!")
secret = random.randint(1, 20)


for x in range(1,6):
    num = int(input("Guess the number: "))
    if (num > 20 or num < 1):
        print("Incorrect Number!")
        continue

    if (num > secret):
        print("Incorrect guess", x, "attempts used")
        print("Too high")
    elif (num < secret):
        print("Incorrect guess,", x, "attempts used")
        print("Too low")
    else:
        print("You guessed the number!")
        print("Number of attempts: ", x)
        break
    
else:
    print("No attempts left, you lose!")
    print("The number was: ", secret)
