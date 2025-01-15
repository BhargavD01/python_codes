#36 The program should generate a random number between 1 and 10. The user guesses until they get it right.
import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Prompt the user to guess until they get it right
guess = None
while guess != random_number:
    guess = int(input("Guess a number between 1 and 10: "))

# When the guess is correct
print("Congratulations! You've guessed the right number:", random_number)