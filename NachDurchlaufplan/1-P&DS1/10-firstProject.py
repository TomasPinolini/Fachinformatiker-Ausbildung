#11 Simple Number Guessing Game
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. You have", max_attempts, "attempts to guess it.")

while attempts < max_attempts:
    # Take the user's guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Check the guess
    if guess == secret_number:
        print("Congratulations! You guessed the correct number in", attempts, "attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    # Display remaining attempts
    print("You have", max_attempts - attempts, "attempts remaining.")

# Game over message
if attempts == max_attempts and guess != secret_number:
    print("Game over! The correct number was:", secret_number)
