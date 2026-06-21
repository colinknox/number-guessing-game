import random

number_to_guess = random.randint(1, 100)
guess_attempts = 0

while True:
    user_guess = int(input("Guess the number (between 1 and 100): "))
    if user_guess > number_to_guess:
        print("Too high!")
        guess_attempts += 1
    elif user_guess < number_to_guess:
        print("Too low!")
        guess_attempts += 1
    else:
        guess_attempts += 1
        if guess_attempts == 1:
            print(f"Congratulations! You guessed the number in {guess_attempts} attempt.")
        else:
            print(f"Congratulations! You guessed the number in {guess_attempts} attempts.")
        break
   