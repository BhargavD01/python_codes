#10 Prompt for principal, rate, and time to calculate compound interest.
principal = float(input("Principal amount: "))
rate = float(input("Rate of interest (in %): "))
time = float(input("Time (in years): "))
n = int(input("Times interest is compounded per year: "))

amount = principal * (1 + rate / 100 / n) ** (n * time)
compound_interest = amount - principal

print("Compound interest:", compound_interest)
print("Total amount:", amount)