import random

while True:
    minimum_value = int(input("Choose a minimum value: "))
    maximum_value = int(input("Choose a maximum value: "))
    if minimum_value > maximum_value:
        print("Minimum value can't be higher than the maximum value.")
    else:
        break

number_to_guess = random.randint(minimum_value, maximum_value)
guess_attempts = 0

while True:
    user_guess = int(input(f"Guess the number (between {minimum_value} and {maximum_value}): "))
    if user_guess > number_to_guess:
        guess_attempts += 1
        print("Too high!")
    elif user_guess < number_to_guess:
        guess_attempts += 1
        print("Too low!")
    else:
        guess_attempts += 1
        if guess_attempts == 1:
            print(f"Congratulations! You guessed the number in {guess_attempts} attempt.")
        else:
            print(f"Congratulations! You guessed the number in {guess_attempts} attempts.")
        break
   