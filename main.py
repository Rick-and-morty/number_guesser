# number guesser keep guessing, you only have 10 numbers
import random
attempts = 0
secret_number = random.randint(1, 10)
print(secret_number)

while True:
    guessed_number = int(input("guess a number 1-10 "))
    if guessed_number > secret_number:
        print("sorry, your number was to high")
        attempts += 1
        print("attempt")
        print(attempts + 1)
    elif guessed_number == secret_number:
        print("good jub dude, you got it!")
        exit()
    else:
        print("sorry your number was to low")
        attempts += 1
        print("attempt")
        print(attempts + 1)

"""
while secret_number > guessed_number:
    if guessed_number == secret_number:
        print("niccceee")
    elif guessed_number > secret_number:
        print("try again your number was to high")
    guessed_number = int(input("guess a number 1_10 "))
else:
    print("try again your number was to low")
"""
