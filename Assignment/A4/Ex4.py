import random
secret = random.randint(1, 10)
guess = int(input("Guess the number (1-10): "))
while guess != secret:
    if guess > secret:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess the number (1-10): "))
print("Correct")