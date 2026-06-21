import random

number_to_guess = random.randint(1, 100)
guess_attempts = 0

while True:
    print(f"DEBUG: Number to guess = {number_to_guess}")
    user_guess = int(input("Guess the number (between 1 and 100): "))
    if user_guess > number_to_guess:
        print("Too high!")
        guess_attempts += 1
    elif user_guess < number_to_guess:
        print("Too low!")
        guess_attempts += 1
    else:
        pass

    print(f"Guess attempts = {guess_attempts}")
        




    # print(f"DEBUG: User guess = {user_guess}")



# Generate a random single number between 1 and 100
# 
# guess_counter = 0
# 
# Loop:
    # Prompt user to guess the number between 1 and 100
    # If the guess is too high:
    #   Print "Too high"
    #   guess_count += 1
    # If the guess is too low:
    #   Print "Too low"
    #   guess_count += 1
    # Else:
    #   Print "Congratulations! You guessed the number in {guess_count} attempts."
    #   break
