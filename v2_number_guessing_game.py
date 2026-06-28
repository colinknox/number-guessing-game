import random

correct_number = random.randint(1, 100)

while True:
    try:
        guess_from_user = int(input("Guess a number between 1 and 100: "))

        if guess_from_user < correct_number:
            print("Too low!")
        elif guess_from_user > correct_number:
            print("Too high!")
        else:
            print("Congratulation! You guessed the right number.")
            break
    except ValueError:
        print("Please input a valid number")
