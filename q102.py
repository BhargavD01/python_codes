#Write a function that randomly selects an element from a given list using the random module.
import random

def select_random_element(input_list):
    return random.choice(input_list) if input_list else None

# Example usage
my_list = [1, 2, 3, 4, 5]
random_element = select_random_element(my_list)
print("Randomly selected element:", random_element)