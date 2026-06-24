import random

high_score = 0


while True:
    print("Welcome to my Number Guessing Game!")

    while True:
        minimum_value = int(input("Choose a minimum value: "))
        maximum_value = int(input("Choose a maximum value: "))
        if minimum_value > maximum_value:
            print("Minimum value can't be higher than the maximum value.")
        else:
            break

    print("You get 5 attempts before it's GAME OVER. Good luck!")

    number_to_guess = random.randint(minimum_value, maximum_value)
    guess_attempts = 0
    max_attempts = 5

    while True:
        if guess_attempts == max_attempts:
            print(f"Game Over! The correct number was {number_to_guess}. Better luck next time!")
            break
        
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
            print(f"HIGH SCORE BEFORE = {high_score}")

            # high_score = guess_attempts
            high_score = guess_attempts
            if guess_attempts < high_score:
                high_score = guess_attempts
            else:
                pass

            print(f"HIGH SCORE AFTER = {high_score}")
            break
    