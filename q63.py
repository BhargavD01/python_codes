#Create a class with a private attribute _balance and provide get_balance() and set_balance() methods.
class Account:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # Private attribute

    def get_balance(self):
        return self._balance  # Return the balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount  # Update the balance if it's non-negative
        else:
            print("Balance cannot be negative.")

account = Account(100)  # Create an account with an initial balance
print("Balance:", account.get_balance())  # Get the balance

account.set_balance(150)  # Set a new balance
print("Updated Balance:", account.get_balance())  # Get the updated balance

account.set_balance(-50)  # Attempt to set a negative balance