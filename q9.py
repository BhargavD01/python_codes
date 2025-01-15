#9 Prompt for principal, rate, and time to calculate simple interest.
principal = float(input("Principal amount: "))
rate = float(input("Rate of interest (in %): "))
time = float(input("Time (in years): "))

simple_interest = principal * rate * time / 100

print("Simple interest:", simple_interest)