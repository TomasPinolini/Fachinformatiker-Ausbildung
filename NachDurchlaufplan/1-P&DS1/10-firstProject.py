#11 Simple Number Guessing Game
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. You have", max_attempts, "attempts to guess it.")

while True:  # Allow restarting the game
    while attempts < max_attempts:
        # Take the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess
        if guess == secret_number:
            print("Congratulations! You guessed the correct number in", attempts, "attempts.")
            break
        elif abs(secret_number - guess) <= 5:
            print("You're very close!")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        # Display remaining attempts
        print("You have", max_attempts - attempts, "attempts remaining.")

    # Game over message
    if attempts == max_attempts and guess != secret_number:
        print("Game over! The correct number was:", secret_number)

    # Ask the user if they want to restart the game
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
    else:
        # Reset the game variables
        secret_number = random.randint(1, 100)
        attempts = 0


# Features
# Random Number Generation: A random number is generated using random.randint().
# User Input: The user guesses a number, which is processed through a loop.
# Feedback System: Provides feedback on whether the guess is too high, too low, or close.
# Attempts Tracking: Tracks the number of attempts and limits them to a maximum.
# Game Over Logic: Ends the game when the user runs out of attempts or guesses correctly.
# Hints for Closeness: Hints the user if the guess is within 5 of the secret number.
# Game Restart Option: Allows the user to restart the game after completion.

# Concepts Applied
# Variables: To store the secret number, user input, attempts count, etc.
# Loops: Used to implement repeated guessing until the user wins or reaches the limit.
# Conditionals: Validate user guesses and provide appropriate feedback.
# Functions: Using random.randint() for number generation.
# User Interaction: Collect user input and provide dynamic feedback.
# Boolean Logic: Combine conditions to check for hints or end-game scenarios.