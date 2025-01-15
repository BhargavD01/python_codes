#Create a class Counter with a class variable count. Implement a @classmethod to increment count and a @staticmethod to display some utility message.
class Counter:
    count = 0  # Class variable

    @classmethod
    def increment(cls):
        cls.count += 1  # Increment the class variable

    @staticmethod
    def display_message():
        return "Utility message from Counter."

# Increment the count
Counter.increment()
Counter.increment()

# Display the current count
print("Current count:", Counter.count)

# Display the utility message
print(Counter.display_message())