import random

def start_game():
    largest_number = 10**156
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {largest_number} (im not).")
    print("Guess the number, and you could win a prize!")

    number_to_guess = random.randint(1, largest_number)
    
    attempts = 0
    max_attempts = 30

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Yay, you got the number (probably using a script but i wont judge ya!) the number was {number_to_guess} and you guessed it in {attempts} attempts.")
                print("You've won a prize! Please contact Goose Industries (just message them or someit) to recieve it!")
                break
        except ValueError:
            print("Please enter a valid number.")
        
        if attempts == max_attempts:
            print(f"Sorry, you've run out of attempts! The correct number was {number_to_guess}. Better luck next time!")

start_game()
